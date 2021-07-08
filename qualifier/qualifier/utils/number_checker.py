def number_checker(input):
    print("Inside fucntion input is : ", input)
    temp = list(input)
    print("Temp is: ", temp)
    print(temp.count('.'))
    if temp.count('.') >= 1:
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
    else:
        input.isnumeric()
        input = int(input)
        print("Input is an INT: ", input)
        return input
