#This program merges two databases of students together
#Nigel Myers
#Fundamentals of Programming
#ACC FALL 2018
#lab10.py
#Prof Onabajo

def addData(file, students):
    filelen = len(file.readlines()); file.seek(0) #get total number of lines, reset pointer to 0
    for i in range(filelen//4): #loop once for each student. Each student has 4 attributes seperated by line breaks. floor division to be safe.
        studentData = [] #initialize studentData so it's not stuck in scope of loop
        for x in range(4): #ID/FirstName/LastName/GPA
            data = file.readline().strip('\n').replace('\"', '') #strip newline and all quotation marks
            try: 
                data = float(data) if '.' in data else int(data) #convert str to float if decimal found, else int. Does not support international
                #Not necessary to convert GPA to float, but if you wanted to sort by GPA, this is still useful to have.
                studentData.append(data) #append data
            except ValueError: #If data is string
                studentData.append(data) #append data
                    
        students.append(studentData) #append list studentData to list students 

            

def main():
    #var initialization
    students = []

    #open and add data. Avoids need for close statement
    with open('BoardmanAnthropologyMajors.txt', 'r') as anthMajors:
        addData(anthMajors, students)
    with open('BoardmanSociologyMajors.txt', 'r') as socMajors:
        addData(socMajors, students)


    students.sort(key = lambda x: x[0]) #Sort by [_][0]

    with open('Combined Students.txt', 'w') as combinedStudents:
        for student in range(len(students)): #loop once for each student array
            for attribute in range(4): #loop once per attribute in array 
                combinedStudents.write('%s \n' % students[student][attribute]) #add attribute

    print('Successfully Merged Student Data')

main()
