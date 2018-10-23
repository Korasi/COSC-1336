class Matrix:
    def __init__(self, matrix, name):
        self.name = name 
        self.matrix = matrix 
        self.summedRows = [sum(row) for row in self.matrix] # calculate sum of every row
        self.summedCols = [sum(array[i] for array in self.matrix) for i in range(len(self.matrix[0]))] # calculate sum of every column
        self.minRows = [min(row) for row in self.matrix] # calculate minimum value in each row
        self.minCols = [min(array[i] for array in self.matrix) for i in range(len(self.matrix[0]))] # calculate maximum value in each row

    #I am so sorry to anyone about to read this spaghetti.
    def printMatrix(self, outputFile = None):
        rowlen = len(self.matrix[0]) 
        output(('%' + str(4 + 5 * rowlen) + 's |  Min |  Sum') % ('Matrix %s' % self.name), outputFile) #print header
        output('     ' + '-' * (5 * rowlen + 13), outputFile) #print a bunch of lines to seperate stuff
        for i, array in enumerate(self.matrix): # repeat for each row in matrix
            output(('     ' + '%4s ' * rowlen + '| %4s | %4s') % (tuple([ele for ele in array] + [self.minRows[i], self.summedRows[i]])), outputFile) #print row of matrix, minimum, and sum of row
        output('     ' + '-' * (5 * rowlen + 13), outputFile) #print a bunch of lines to seperate stuff
        output('Min: ' + '%4s ' * len(self.minCols) % (tuple(ele for ele in self.minCols)), outputFile) #print minimum of each col
        output('Sum: ' + '%4s ' * len(self.summedCols) % (tuple(ele for ele in self.summedCols)), outputFile) #print sum of each col
        output('', outputFile) #newline break

def multiplyMatrices(matrixX, matrixY):
    rotatedY = list(zip(*matrixY)) #rewrite matrixY so row[i] = column[i]
    #multiply matrices. It's a complcated process of 3 nested loops on one line.
    return [[sum(X * Y for X, Y in zip(rowX, colY)) for colY in rotatedY] for rowX in matrixX] 

def loadRows(file, n): 
    # n = elements per row
    data = [int(x) for x in file.read().strip('\n').split(' ')] # split string into list and convert to int
    return [data[i:i+n] for i in range(0, len(data), n)] # split list 'data' into list of lists of length n

def loadColumns(file, n):
    # n = number of rows
    data = [int(x) for x in file.read().strip('\n').split(' ')] # split string into list and convert to int
    return [data[i::n] for i in range(n)] # split list 'data' into list of 3 lists, taking every nth element

def output(string, file = None):
    print(string)
    if file:
        file.write('%s\n' % string)

def main():
    x = y = z = None

    #Assign Matrix objects
    with open('MatrixX.txt', 'r') as inputFile:
        x = Matrix(loadRows(inputFile, 3), 'X') # create Matrix 'X' from input file, 3 elements per row
    with open('MatrixY.txt', 'r') as inputFile:
        y = Matrix(loadColumns(inputFile, 3), 'Y') # create Matrix 'Y' from input file, 3 rows

    #Multiply matrixes X and Y, and set as Matrix 'Z'
    z = Matrix(multiplyMatrices(x.matrix, y.matrix), 'Z') 

    # Print each matrix to output file
    with open('Lab5_Output.txt', 'w') as outputFile:
        x.printMatrix(outputFile)
        y.printMatrix(outputFile)
        z.printMatrix(outputFile)

        #print sum of the two specific dimensions because its part of the assignment
        output('Sum of X[_][2] and Y[2][_] = %s' % (x.summedCols[2] + y.summedRows[2]), outputFile)
        
main()

