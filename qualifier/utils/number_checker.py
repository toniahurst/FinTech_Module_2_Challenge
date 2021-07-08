"""Number Checker

This script takes user input and converts it 
to an integer, float or error.
"""

def number_checker(input):  
    """Finds type of input (in, float, other).

    Args:
        input : a string of alphanumeric characters
    Returns:
        input : the string converted to an int, float 
        or error message depending on contents of string.
    """
    # handling an integer
    if input.isnumeric():
        input = int(input)
        return input
    else:
        # input is a float or its a mix of other chars
        try:
            # is the input a float?
            input = float(input)
            return input
        except ValueError:
            # input is something else
            print("This app requires numeric data.")
            return False
    