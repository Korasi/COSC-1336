
# This program computes payroll over multiple departments given employee data
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab9.py
# Prof Onabajo

class Department: 
    def __init__(self, name, employees = None):
        #init class variables
        self.name = name
        self.employees = [] if not employees else employees #empty list unless specified otherwise
        self.payroll = 0

    def calculatePayroll(self):
        self.payroll = 0 #reset payroll to 0 prior to calculation
        for employee in self.employees: #loop once for each employee
            self.payroll += employee[0] * employee[1] #increment department payroll by employee wage * hours worked

    def addEmployee(self, salary, hours):
        self.employees.append([salary, hours]) #add employee to list employees

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
    departmentNames = ['Personnel', 'Marketing', 'Manufacturing', 'Computer Services', 'Sales', 'Accounting', 'Shipping']
    departments = [Department(name) for name in departmentNames] #init list of 7 department objects
    
    while True: #infinite loop
        department = validateInt('\nWhat department is the employee in (type "0" to exit)? ', 0, 7) #get department number or termination input
        if department == 0:
            break #terminate loop
        
        #get employee payroll info
        salary = validateData('What is the employee\'s hourly salary? ', 0)
        hours = validateData('How many hours did the employee work? ', 0)

        #store employee data in class department.employees
        departments[department - 1].addEmployee(salary, hours)
    
    grossPayroll = 0
    print('')

    for department in departments: #loop for each object in list departments
        department.calculatePayroll() #calculate payroll
        grossPayroll += department.payroll #increment gross payroll

        print('Gross payroll the %s department: %.2f' % (department.name, department.payroll)) #print payroll of the department

    print('\nTotal gross payroll: %.2f' % grossPayroll) #print total payroll
    
main()

