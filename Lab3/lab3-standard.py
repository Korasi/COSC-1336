# This program computes batting and slugging averages from a given csv file of player data.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab3-standard.py
# Prof Onabajo

# Version: input .txt; output .txt

#import csv and datetime modules
import csv
from datetime import datetime
			

def main():
    #open input and output files
    input_file = open('playerdata.txt', 'r')
    output_file = open('Batting_Output.txt', 'w')
    
    output_file.write('\n%s\n' % datetime.now().strftime('%Y/%m/%d - %H:%M:%S')) #timestamp the date/time of output

    while True:
        try:
            #Assign variables for each value in row of txt [Singles, Doubles, Triples, Home Runs, At Bat]
            row = input_file.readline().strip('\n').split(',')
            playernumber, singles, doubles, triples, homeruns, atbat = map(int, row)

            #Calculate Batting and Slugging averages
            batavg = (singles + doubles + triples + homeruns) / atbat
            slugavg = (singles + doubles * 2 + triples * 3 + homeruns * 4) / atbat #multiply double/triple/hr by base value
            
            #print all data
            print('Player %s | Singles: %i | Doubles: %i | Triples: %i | Home Runs: %i | At Bat: %i | Batting Avg: %.3f | Slugging Avg: %.3f\n' % (playernumber, singles, doubles, triples, homeruns, atbat, batavg, slugavg))
            output_file.write('Player %s | Singles: %i | Doubles: %i | Triples: %i | Home Runs: %i | At Bat: %i | Batting Avg: %.3f | Slugging Avg: %.3f\n' % (playernumber, singles, doubles, triples, homeruns, atbat, batavg, slugavg))
        except (ValueError, IndexError): # EOF Reached, break out of infinite loop
            break

    #close input and output files
    input_file.close()
    output_file.close() 

main()
