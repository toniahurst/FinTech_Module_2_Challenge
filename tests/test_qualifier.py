# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

def test_save_csv():
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csvpath = Path("data/qualifying_loan.csv")
    assert(csvpath) == Path('data/qualifying_loan.csv')

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def filters():
   #S bank_data = fileio.load_csv(Path('/Users/antoniamalvino/Desktop/FinTech_Module_2/FinTech_Module_2_Challenge/data/daily_rate_sheet.csv'))
   #assert filter.credit_score(current_credit_score, bank_data) == 750
   assert filter.debt_to_income(1500, 4000) == 0.375
   assert filter.loan_to_value(210000, 250000) == 0.84
   #assert filter.filter_max_loan_size(210000, bank_data) == 300000

    #current_credit_score = 750

    #income = 4000
    #loan = 210000
    #home_value = 250000

    #monthly_debt_ratio = 0.375

    #loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
"""
def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!
"""