
# This program computes payroll over multiple departments given employee data
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab9.py
# Prof Onabajo

def getDepartment(message):
    while True: #infinite loop
        try:
            department = int(confirmData(message, minimum = 1, maximum = 7, allowStop = True)) #attempt to convert float to int, value 1-7 only. -1 if terminate loop in main
        except ValueError: #could not convert float to int, invalid
            print('This is not a valid number. Try again.')
        else: #successfully convert float to int, valid input; return input
            return department

def confirmData(message, minimum = 0, maximum = float('inf'), allowStop = False):
    while True: #infinite loop
        try:
            data = input(message)
            # if allowed to terminate and input is 'stop' after stripping any periods and spaces, return -1 to terminate loop in main
            if allowStop and data.lower().replace('.','').replace(' ','') == 'stop':
                return -1
            data = float(data) #convert input to float
            if data < minimum or data > maximum: #ensure data is between minimum and maximum values (default: min 0, max infinity)
                print('This is not a valid number. Try again.') 
                continue #return to parent loop
        except ValueError: #not a float
            print('This is not a valid number. Try again.') 
        else: #valid input; return data
            return data
            

def main():
    departments = [[0] for x in range(7)] #create list of 7 lists of [0, None]
    names = ['Personnel', 'Marketing', 'Manufacturing', 'Computer Services', 'Sales', 'Accounting', 'Shipping'] #department names. department i: names[i-1]
    
    while True: #infinite loop
        department = getDepartment('What department is the employee in (type "stop" to exit)? ') #get department number or termination input
        if department == -1:
            break #terminate loop
        #get employee payroll info
        salary = confirmData('What is the employee\'s hourly salary? ')
        hours = confirmData('How many hours did the employee work? ')
        #store info as third dimension in departments[department - 1]. Could calculate here to avoid extra lists
        departments[department - 1].append([salary, hours])

    #init gross payroll 
    grossPayroll = 0
    
    for i in range(7): #loop once per department
        for x in range(1, len(departments[i])): #loop once for each list in list 'departments', starting at 1. loops 1 to length - 1
            departments[i][0] += departments[i][x][0] * departments[i][x][1]
            # departments[i] is the ID of the department - 1
            # departments[i][0] is payroll for that department.
            # department[i][x if x > 0] is an employee's data, as list [salary, hours]
            # increment department payroll by employee[salary] * employee[hours]
        grossPayroll += departments[i][0] # increment gross payroll by department payroll 
        print('Gross payroll the %s department: %.2f' % (names[i].lower(), departments[i][0])) #print payroll of the department

    print('Total gross payroll: %.2f' % grossPayroll) #print total payroll
    

main()
