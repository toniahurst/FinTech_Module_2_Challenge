# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.qualifier.utils import fileio

# Import Calculators
from qualifier.qualifier.utils import calculators

# Import Filters
from qualifier.qualifier.filters import credit_score
from qualifier.qualifier.filters import debt_to_income
from qualifier.qualifier.filters import loan_to_value
from qualifier.qualifier.filters import max_loan_size

def test_save_csv():
    # ******* Finish this
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    #def test_save_csv():
        #assert(csvpath) == Path('../data/output/qualifying_loans.csv').exists()
    """csvpath = Path("../data/output/qualifying_loans.csv")
    fileio.save_csv(csvpath)
    assert(csvpath) == Path('../data/output/qualifying_loans.csv').exists()
"""
    """
    file = open("/Users/antoniamalvino/Desktop/FinTech_Module_2_Challenge/qualifier/data/qualifying_loans.csv",'r')
    expected = ["lender", "max_loan_amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest_Rate"]
    assert expected==file.readline().rstrip().split(",")
    """
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84


def test_filters():
    # bank_data = fileio.load_csv(Path('./qualifier/data/daily_rate_sheet.csv'))
    assert filter.credit_score(750) == 750
    #assert filter.filter_debt_to_income(0.375, bank_data) == 0.375
    #assert filter.filter_loan_to_value(loan_to_value_ratio, bank_data) == 0.84
    #assert filter.filter_max_loan_size(loan_amount, bank_data) ==

    current_credit_score = 750

    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
    # YOUR CODE HERE!

   