# This program computes batting and slugging averages from a given csv file of player data.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab3-parsecsv.py
# Prof Onabajo

# Version: import .csv; output .txt

#import csv and datetime modules
import csv
from datetime import datetime


def main():
    #open playerdata.csv
    input_file = csv.DictReader(open('playerdata.csv'))

    #open batting output file, or create if it doesn't exist
    output_file = open('Batting_Output.txt', 'w')
    
    output_file.write('\n%s\n' % datetime.now().strftime('%Y/%m/%d - %H:%M:%S')) #timestamp the date/time of output
    
    for row in input_file: #repeat section for each row in CSV
        #Assign variables for each value in csv. Singles, Doubles, Triples, Home Runs, At Bat
        playernumber = row['playernumber']
        singles = int(row['singles'])
        doubles = int(row['doubles'])
        triples = int(row['triples'])
        homeruns = int(row['homeruns'])
        atbat = int(row['atbat'])

        #Calculate Batting and Slugging averages
        batavg = (singles + doubles + triples + homeruns) / atbat
        slugavg = (singles + doubles * 2 + triples * 3 + homeruns * 4) / atbat #multiply double/triple/hr by base value
        
        #print all data
        print('Player %s | Singles: %i | Doubles: %i | Triples: %i | Home Runs: %i | At Bat: %i | Batting Avg: %.3f | Slugging Avg: %.3f\n' % (playernumber, singles, doubles, triples, homeruns, atbat, batavg, slugavg))
        output_file.write('Player %s | Singles: %i | Doubles: %i | Triples: %i | Home Runs: %i | At Bat: %i | Batting Avg: %.3f | Slugging Avg: %.3f\n' % (playernumber, singles, doubles, triples, homeruns, atbat, batavg, slugavg))

    #close file
    output_file.close() 

main()

