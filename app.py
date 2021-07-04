# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

Example:
    $ python app.py
"""
import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.qualifier.utils.fileio import load_csv, save_csv


from qualifier.qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.qualifier.filters.credit_score import filter_credit_score
from qualifier.qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.qualifier.filters.loan_to_value import filter_loan_to_value


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """
    print("\n" * 40)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n" * 2)
    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    print("")
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find the path you provided: {csvpath}")

    return load_csv(csvpath)


def get_applicant_info():
    """Prompt dialog to get the applicant's financial information.

    Returns:
        Returns the applicant's financial information.
    """

    credit_score = int(questionary.text("Enter a credit score between 300 and 850: ").ask())
    if credit_score < 300 or credit_score > 850:
        print("\u001b[31m", "\n")
        print("Credit score must be between 300 and 850.", "\n")
        print("Exiting system...", "\u001b[0m")
        exit()
    else:
        True

    debt = float(questionary.text("What's your current monthly debt? ").ask())
    if debt < 0:
        print("\u001b[31m", "\n")
        print("Monthly debt must be greater than or equal to 0.", "\n")
        print("Exiting system...", "\u001b[0m", "\n")
        exit()
    else:
        True

    income = float(questionary.text("What's your total monthly income?").ask())
    if income < 0:
        print("\u001b[31m", "\n")
        print("Monthly INCOME must be greater than 0.", "\n")
        print("Exiting system...", "\u001b[0m", "\n")
        exit()
    else:
        True

    loan_amount = float(questionary.text("What's your desired loan amount?").ask())
    if loan_amount < 0:
        print("\u001b[31m", "\n")
        print("Loan amount must be greater than 0.", "\n")
        print("Exiting system...", "\u001b[0m", "\n")
        exit()
    else:
        True

    home_value = float(questionary.text("What's your home value?").ask())
    if home_value < 0:
        print("\u001b[31m", "\n")
        print("Monthly debt must be greater than or equal to 0.", "\n")
        print("Exiting system...", "\u001b[0m", "\n")
        exit()
    else:
        True

    return credit_score, debt, income, loan_amount, home_value



def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
    """Determine which loans the user qualifies for.

    Loan qualification criteria is based on:
        - Credit Score
        - Loan Size
        - Debit to Income ratio (calculated)
        - Loan to Value ratio (calculated)

    Args:
        bank_data (list): A list of bank data.
        credit_score (int): The applicant's current credit score.
        debt (float): The applicant's total monthly debt payments.
        income (float): The applicant's total monthly income.
        loan (float): The total loan amount applied for.
        home_value (float): The estimated home value.

    Returns:
        A list of the banks willing to underwrite the loan.

    """

    # Calculate the monthly debt ratio
    monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n", "\u001b[34;1m")
    print(f"------->>>  Monthly debt-to-income ratio is {monthly_debt_ratio:.02f}")
    print("\u001b[0m")

    # Calculate loan to value ratio
    loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
    print("\n", "\u001b[34;1m")
    print(f"------->>>  Loan-to-value ratio is {loan_to_value_ratio:.02f}.")
    print("\n", "\u001b[0m")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")

    # Run qualification filters
    bank_data_filtered = filter_max_loan_size(loan, bank_data)
    bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)
    bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
    print("", "\u001b[32m")
    print(f"The client qualifies for {len(bank_data_filtered)} loans.")
    print("\u001b[0m")

    return bank_data_filtered


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # Usability dialog for savings the CSV Files.

    save_file = questionary.text("Would you like to save these loans to a file? y or n: ").ask()
    print("\n")
    if save_file == "y":
        file_name = questionary.text("Please name your file using snake_case and ending in csv. Ex: my_loans.csv").ask()
        print("\n")
        csvpath = Path(file_name)
        save_csv(qualifying_loans, csvpath)
        print("Your file", "\u001b[32m", (csvpath), "\u001b[0m", "has been saved to: ", "\u001b[32m", csvpath.absolute(),  "\u001b[0m")
        clean = ["Your file", "\u001b[32m", (csvpath), "\u001b[0m", "has been saved to: ", "\u001b[32m", csvpath.absolute(),  "\u001b[0m"]
        clean = clean.strip()
        print(clean)
        print("\n")
        
    else:
        print("Your file will NOT be saved. Goodbye", "\n")
    print("* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
    print("\n")
   

     

def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    save_qualifying_loans(qualifying_loans)


    



if __name__ == "__main__":
    fire.Fire(run)
