# This program computes statistics from a list of test scores
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab1.py
# Prof Onabajo

#todo: comments

def output(string, outfile):
    print(string)
    outfile.write('%s\n' % string)

def floatToString(input_):
    return ('%f' % input_).rstrip('0').rstrip('.')


def the_average_distance_of_each_data_point_from_the_mean_squared_then_square_rooted_to_remove_the_negative_sign_also_known_as_the_standard_deviation(scores, mean):
    std = 0
    for score in scores:
        dev = mean - score
        std += dev ** 2 
    return (std / len(scores)) ** .5
        

def main():
    sum_, mean, dev2, std, sd2 = 0, 0, 0, 0, 0
    scores = []
    
    with open('testscores.txt', 'r') as inputFile:  
        while True:
            try:
                row = inputFile.readline().strip('\n').split(',')
                student, score = row[0], int(row[1].strip(' '))

                sum_ += score
                scores.append(score)
            except (IndexError, ValueError):
                break

    mean = sum_ / len(scores)

    std = the_average_distance_of_each_data_point_from_the_mean_squared_then_square_rooted_to_remove_the_negative_sign_also_known_as_the_standard_deviation(scores, mean)

    with open('Lab4_Output.txt', 'w') as outputFile:
        output('%12s %12s %12s\n' % ('DEV', 'DEV1', 'SD1'), outputFile)
        for score in scores:
            dev = mean - score
            dev1 = dev ** 2
            dev2 += dev1
            sd1 = dev / std
            sd2 += sd1

            output('%12s %12s %12s' % (floatToString(dev), floatToString(dev1), floatToString(sd1)), outputFile)

        output('\nSum:%s          Mean: %s          STD: %s' % (floatToString(sum_), floatToString(mean), floatToString(std)), outputFile)
        output('Sum of DEV1: %s          Sum of SD1: %s' % (floatToString(dev2), floatToString(sd2)), outputFile)

    print('\nOutput written to Lab4_Output.txt')

main()
