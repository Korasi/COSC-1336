# This program computes the cost of a house over five years given initial, fuel, and tax costs.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab2.py
# Prof Onabajo

def getInput(text, requireInt = False): #Get input from user. Float unless optional variable is true, in which case int
    while True:
        try:
            number = int(input(text)) if requireInt else float(input(text))
        except ValueError:
            print('This is not a number. Try again.')
        else:
            return number


def main():
    #init variables
    initial, annual, tax, total = 0, 0, 0, 0 
    houses = []

    for i in range(getInput('How many houses do you want to calculate the cost of? ', requireInt = True)):
        #set variables
        initial = getInput('Please enter the initial cost of the house. ')
        annual = getInput('Please inter the annual fuel cost of the house. ')
        tax = getInput('Please enter the tax rate of the house. ')

        #calculate total price over five years and append to list 'houses'
        houses.append(initial + annual * 5 + initial * tax * 5)
    #print data    
    for i in range(len(houses)):
        print('The total cost of house %i over five years is %.2f' % (i + 1, houses[i]))
main()
