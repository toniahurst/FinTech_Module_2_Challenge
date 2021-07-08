def number_checker(input):
    
    print("Inside fucntion input is : ", input)
    # handling an integer
    if input.isnumeric():
        print("Input is ", input)
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
            print("Not a float")
            return False
    