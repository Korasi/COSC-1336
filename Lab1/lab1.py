# This program computes the box office profits of a movie
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab1.py
# Prof Onabajo

def main():
    #init vars
    adult, children, adultprice, childrenprice = 0, 0, 6, 3
    name, gross, paid, net = 0, 0, 0, 0
    #get user input
    name = str(input('Please enter the name of the movie: '))
    children = int(input('How many child tickets sold? '))
    adult = int(input('How many adult tickets sold? '))
    #calculate profits and costs
    gross = children * childrenprice + adult * adultprice
    net = round(gross * .2, 2)
    paid = gross - net

    #print data
    print('Movie Name: ' + name)
    print('Adult Tickets Sold: ', adult)
    print('Child Tickets Sold: ', children)
    print('Gross Box Office Profit: $%.2f' % gross)
    print('Net Box Office Profit: $%.2f' % net)
    print('Amount Paid to Movie Co: $%.2f' % paid)
    
main()
          
