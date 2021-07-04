# import calculators

from qualifier.utils import calculators

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(500, 10000) == 0.05

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84
