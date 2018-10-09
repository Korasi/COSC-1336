# This program computes statistics from a list of test scores
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab4-wth-objects.py
# Prof Onabajo

#init global vars
global _mean, _std 

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = int(score)
        self.dev = 0
        self.dev1 = 0
        self.sd1 = 0

    #calculate DEV and DEV1
    def calculateDEV1(self):
        global _mean
        self.dev = _mean - self.score
        self.dev1 = self.dev ** 2
        return self.dev1

    #calculate SD1
    def calculateSD1(self):
        global _std
        self.sd1 = self.dev / _std
        return self.sd1
        

def output(string, outfile): #print output to console and data file
    print(string)
    outfile.write('%s\n' % string)

def floatToString(input_): #convert float to string, removing trailing zeros and decimal
    return ('%f' % input_).rstrip('0').rstrip('.')
        
def main():
    #init variables
    global _mean, _std
    _sum, dev2, sd2 = 0, 0, 0
    students = []
    
    with open('testscores.txt', 'r') as inputFile: #open input file (with open as _ removes the need for closing statements)
        while True: #infinite loop
            try:
                row = inputFile.readline().strip('\n').split(',') #strip newline, split by comma. [Student i, testScore]
                students.append(Student(row[0], row[1].strip(' '))) #add object Student(name, score) to list students
            except (IndexError, ValueError): #reached end of file
                break #break out of loop

    _sum = sum(student.score for student in students) #for each object in array students, sum the object's score attribute
    _mean = _sum / len(students) #calculate mean
    dev2 = sum(student.calculateDEV1() for student in students) #for each object in array students, calculate DEV1 (and DEV), and sum them
    _std = (dev2 / len(students)) ** .5 #calculate STD; sqrt(DEV2 / amount of indexes in array students)
            

    with open('Lab4_Output.txt', 'w') as outputFile: #open output file (with open as _ removes the need for closing statements)
        output('%8s %12s %12s %12s\n' % ('Score', 'DEV', 'DEV1', 'SD1'), outputFile) #headers
        for student in students: #loop for each object in students array
            output('%8s %12s %12s %12s' % (student.score, floatToString(student.dev), floatToString(student.dev1), floatToString(student.calculateSD1())), outputFile) #output and right align DEV, DEV1, SD1 (and calculate SD1)

        sd2 = sum(student.sd1 for student in students) #for each object in array students, sum the object's sd1 attribute
        
        output('\nSum:%s          Mean: %s          STD: %s' % (floatToString(_sum), floatToString(_mean), floatToString(_std)), outputFile) #output Sum, Mean, Standard Deviation
        output('Sum of DEV1: %s          Sum of SD1: %s' % (floatToString(dev2), floatToString(sd2)), outputFile) #output Sum of deviations from the main, Sum of standard scores (should always be 0)
        
    print('\nOutput written to Lab4_Output.txt')

main()
