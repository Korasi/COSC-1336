'''
This program utilizes merge sort and binary serach
Fundamentals of Programming
Nigel Myers
ACC FALL 2018
Lab7.py
Prof Onabajo
'''

# Going by the instruction of the assignment, I wrote it; not implemented 
def insertionSort(data, slot=-1):
    slot = len(data) - 1 if slot == -1 else slot #if slot is not defined, set slot = length of list - 1
    if slot > 0: #only do if slot > 0, can only sort starting from second index.
        insertionSort(data, slot - 1) #recursively call the function until slot = 1
        tosort = data[slot] #store value of slot to store in temporary value.
        i = slot - 1 #start sort attempts from the slot before it
        while i >= 0 and data[i] > tosort: #loop as long as the slot it's checking >= 0, and if the value we're checking is smaller than the value we check
            data[i + 1] = data[i] #shift the index we're checking over to the next value of the list
            i -= 1 # iterate i down
        data[i + 1] = tosort #if the value we're sorting is less than the value we checked, insert value

# Implemented sort function
def mergeSort(array):
    if len(array) > 1: #check list length is >1, else the list is sorted already
        mid = len(array) // 2 #find the mid point of the list

        #split list into two halves
        lefthalf = array[:mid] 
        righthalf = array[mid:] 

        #recursively call merge sort on the halves 
        mergeSort(lefthalf) 
        mergeSort(righthalf)

        i_main, i_left, i_right = 0, 0, 0

        # repeat while both halves have remaining indeces
        while i_left < len(lefthalf) and i_right < len(righthalf): 
            if lefthalf[i_left] < righthalf[i_right]: #if lefthalf iteration < righthalf iteration, place left into list
                array[i_main] = lefthalf[i_left]
                i_left += 1 #increment lefthalf
            else: #if righthalf iteration < lefthalf iteration, place right into list
                array[i_main] = righthalf[i_right]
                i_right += 1 #increment righthalf
            i_main += 1

        # no more indeces left in one list, other half is always already sorted. insert at the end
        while i_left < len(lefthalf):
            array[i_main] = lefthalf[i_left]
            i_main += 1
            i_left += 1
        while i_right < len(righthalf):
            array[i_main] = righthalf[i_right]
            i_main += 1
            i_right += 1

def parseCSV(filename, delimiter=','):
    # Usage: parseCSV(filename[, delimiter])
    with open(filename, 'r') as csv: #open file in read only
        csv_data = [] #init empty list
        header = csv.readline().strip('\n').split(delimiter) #split csv header by delim
        while True: #infinite loop
            row = csv.readline().strip('\n').split(delimiter) #split row by delim
            if len(row) == 1 and not row[0]: #if only one attribute in row, and row[0] is an empty string, treat as end of CSV
                return csv_data #return csv_data list 
            csv_data.append([int(item) for item in row])
    

def binarySearch(data, search):
    left, right = 0, len(data) - 1
    while left < right: 
        slot = (left + right) // 2 # find the midpoint of the search range
        if data[slot][0] < search: # if the spot checked is less than the search, shift leftmost search boundary to right of slot
            left += 1 
        elif data[slot][0] > search: # if the spot checked is greater than the search, shift rightmost boundary to left of slot
            right -= 1 
        else: # number is equal to search value.
            return slot 
    return -1 

def changeScores(students, newScores): 
    for newScore in newScores: #loop for each score in the updated scores
        index = binarySearch(students, newScore[0]) #get index of the student ID to update the score of
        print('Changing index %s id %s to score %s' % (index, students[index][0], newScore[1])) 
        students[index][1] = newScore[1] #update the score of the student

def outputScores(students, outputFile = None):
    output('%s,%s' % ('ID', 'Score'), outputFile) 
    [output('%s,%s' % (tuple(student)), outputFile) for student in students]

def output(string, outputFile = None):
    print(string)
    if outputFile:
        outputFile.write('%s\n' % string)
    

def main():
    students = parseCSV('Student_Data.txt')
    newScores = parseCSV('New_Data.txt')

    mergeSort(students)

    changeScores(students, newScores)
    with open('Lab7_Output.csv', 'w') as outputFile:
        outputScores(students, outputFile)
        
main()
