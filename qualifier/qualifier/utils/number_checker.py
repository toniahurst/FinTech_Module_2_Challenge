def number_checker(input):
    
    print("Inside fucntion input is : ", input)
    # handling an integer
    if input.isnumeric():
        print("Input is ", input)
        input = int(input)
        return input
    else:
        # input is a float or its a mix of other chars
        print ("Input is: ", input)

            # is the input a float?
        try:
            print ("This IS a float: ", float(input))
            input = float(input)
            return input
            # return True
        except ValueError:
            print("Not a float")
            return False
    