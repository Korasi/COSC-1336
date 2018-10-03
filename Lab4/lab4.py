# This program computes statistics from a list of test scores
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab4.py
# Prof Onabajo

def output(string, outfile): #print output to console and data file
    print(string)
    outfile.write('%s\n' % string)

def floatToString(input_): #convert float to string, removing trailing zeros and decimal
    return ('%f' % input_).rstrip('0').rstrip('.')


def the_average_distance_of_each_data_point_from_the_mean_squared_then_square_rooted_to_remove_the_negative_sign_also_known_as_the_standard_deviation(scores, mean): #calculate standard deviation
    std = 0
    for score in scores: #loop once for each test score
        dev = mean - score #calculate deviation from the mean
        std += dev ** 2 #square the deviation from the mean to remove negative, and add it to the sum of the squared means
    return (std / len(scores)) ** .5 #return the square root the squared means; the standard deviation
        

def main():
    #initialize variables
    sum_, mean, dev2, std, sd2 = 0, 0, 0, 0, 0 
    scores = []
    
    with open('testscores.txt', 'r') as inputFile: #open input file (with open as _ removes the need for closing statements)
        while True: #infinite loop
            try:
                row = inputFile.readline().strip('\n').split(',') #strip newline, split by comma. [Student i, testScore]
                score = int(row[1].strip(' ')) #strip space from score, convert to int

                sum_ += score #increment sum by score
                scores.append(score) #add score to array of scores
            except (IndexError, ValueError): #reached end of file
                break #break out of loop

    mean = sum_ / len(scores) #calculate mean

    std = the_average_distance_of_each_data_point_from_the_mean_squared_then_square_rooted_to_remove_the_negative_sign_also_known_as_the_standard_deviation(scores, mean) #get standard deviation

    with open('Lab4_Output.txt', 'w') as outputFile: #open output file (with open as _ removes the need for closing statements)
        output('%8s %12s %12s %12s\n' % ('Score', 'DEV', 'DEV1', 'SD1'), outputFile) #headers
        for score in scores: #loop for each score in scores array
            dev = mean - score #calculate deviation from the mean
            dev1 = dev ** 2 #calculate the square of the deviation from the mean
            dev2 += dev1 #increment sum of squares of the deviation from the mean by dev1
            sd1 = dev / std #calculate the standard score
            sd2 += sd1 #increment the sum standard scores by sd1

            output('%8s %12s %12s %12s' % (score, floatToString(dev), floatToString(dev1), floatToString(sd1)), outputFile) #output and right align DEV, DEV1, SD1

        output('\nSum:%s          Mean: %s          STD: %s' % (floatToString(sum_), floatToString(mean), floatToString(std)), outputFile) #output Sum, Mean, Standard Deviation
        output('Sum of DEV1: %s          Sum of SD1: %s' % (floatToString(dev2), floatToString(sd2)), outputFile) #output Sum of deviations from the main, Sum of standard scores (should always be 0)

    print('\nOutput written to Lab4_Output.txt')

main()
