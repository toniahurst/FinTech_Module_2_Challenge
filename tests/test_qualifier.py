# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import filters

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/qualifying_loans.csv
    file = open("/Users/antoniamalvino/Desktop/FinTech_Module_2/FinTech_Module_2_Challenge/data/daily_rate_sheet.csv",'r')
    expected = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]
    assert expected==file.readline().rstrip().split(",")

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    #bank_data = fileio.load_csv(Path('../data/daily_rate_sheet.csv'))
    # bank_data to test credit score filter
    bank_data = [["FHA Fredie Mac - Premier Option","600000","0.9","0.43","790","3.6"], ["Bank of Big - Premier Option","300000","0.85","0.47","740","3.6"]]
    assert filters.filter_credit_score(current_credit_score, bank_data) == [["Bank of Big - Premier Option","300000","0.85","0.47","740","3.6"]]
    # Bank data to test debt to income filter
    bank_data = [["Bank of Big - Premier Option","300000","0.85","0.47","740","3.6"],["West Central Credit Union - Premier Option","400000","0.9","0.35","760","2.7"]]
    assert filters.filter_debt_to_income(monthly_debt_ratio, bank_data) == [["Bank of Big - Premier Option","300000","0.85","0.47","740","3.6"]]
    # Bank to test loan to value
    bank_data = [["Goldman MBS - Premier Option","500000","0.8","0.4","770","3.6"],["Citi MBS - Premier Option","400000","0.9","0.47","780","3.6"]]
    assert filters.filter_loan_to_value(loan_to_value_ratio, bank_data) == [["Citi MBS - Premier Option","400000","0.9","0.47","780","3.6"]]
    #Bank data to test max loan size
    bank_data = [["FHA Fannie Mae - Starter Plus","200000","0.9","0.37","630","4.2"], ["General MBS Partners - Starter Plus","300000","0.85","0.36","670","4.05"]]
    assert filters.filter_max_loan_size(loan, bank_data) == [["General MBS Partners - Starter Plus","300000","0.85","0.36","670","4.05"]]



current_credit_score = 750
debt = 1500
income = 4000
loan = 210000
home_value = 250000

monthly_debt_ratio = 0.375

loan_to_value_ratio = 0.84
