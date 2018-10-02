# This program computes the cost of a house over five years given initial, fuel, and tax costs.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab2.py
# Prof Onabajo


def validateData(displayText, *args): #prompt user for input, and validate if it's int or float
    # Usage: validateData(displayText[, minimumValue[, maximumValue]])
    minimum = args[0] if len(args) >= 1 and isinstance(args[0], (float, int)) else float('-INF') #-inf default, args[0] if specified
    maximum = args[1] if len(args) >= 2 and isinstance(args[1], (float, int)) else float('INF') #inf default, args[1] if specified
    while True: #loop infinitely 
        try:
            data = input(displayText) #get user input
            data = float(data) if '.' in data else int(data) #convert to float if decimal in string, else convert to int
            if data < minimum or data > maximum: #if outside of range
                print('This is an invalid number')
                continue #return to start of loop
        except ValueError: #if value error, alert user and loop back
            print('This is not a number.')
        else: #valid data; return data
            return data

def validateInt(displayText, *args): #prompt user for input, and validate that datatype to be int
    # Usage: validateInt(displayText[, minimumValue[, maximumValue]])
    while True: #infinite loop
        data = validateData(displayText, *args) #get input from validateData()
        if not isinstance(data, int): #if data is not int, then alert user and re-loop
            print('This is not an integer.')
            continue
        return data #is int; return data


def main():
    #init variables
    initial, annual, tax, total = 0, 0, 0, 0 
    houses = []

    for i in range(validateInt('How many houses do you want to calculate the cost of? ', 0)):
        #set variables
        initial = validateData('Please enter the initial cost of the house. ', 0)
        annual = validateData('Please inter the annual fuel cost of the house. ', 0)
        tax = validateData('Please enter the tax rate of the house. ', 0)

        #calculate total price over five years and append to list 'houses'
        houses.append(initial + annual * 5 + initial * tax * 5)
    #print data    
    for i in range(len(houses)):
        print('The total cost of house %i over five years is %.2f' % (i + 1, houses[i]))
main()
