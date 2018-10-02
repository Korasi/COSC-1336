# This program computes the box office profits of a movie
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab1.py
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

def output(string, outfile): #combine print and outfile.write statments into one function
    print(string)
    outfile.write('%s\n' % string)

def main():
    #init variables
    adult, children, adultprice, childrenprice = 0, 0, 6, 3
    name, gross, paid, net = '', 0, 0, 0
    
    #prompt input
    name = str(input('Please enter the name of the movie: '))
    children = validateInt('How many child tickets sold? ', 0)
    adult = validateInt('How many adult tickets sold? ', 0)
    
    #calculate profits
    gross = children * childrenprice + adult * adultprice
    net = round(gross * .2, 2)
    paid = gross - net

    #print data and output data to file
    with open('Lab1_Output.txt', 'w') as outfile: # with .. as .. prevents need to closefile
        output('Movie Name: %s' % name, outfile)
        output('Adult Tickets Sold: %i' % adult, outfile)
        output('Child Tickets Sold: %i' % children, outfile)
        output('Gross Box Office Profit: %.2f' % gross, outfile)
        output('Net Box Office Profit: %.2f' % net, outfile)
        output('Amount Paid to Movie Co: %.2f' % paid, outfile)
main()
          
