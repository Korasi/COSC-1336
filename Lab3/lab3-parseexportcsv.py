# This program computes batting and slugging averages from a given csv file of player data.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab3-parseexportcsv.py
# Prof Onabajo

#version: Import .csv; export .txt

#import csv and datetime modules
import csv
from datetime import datetime


def main():
    #open playerdata.csv
    input_file = csv.DictReader(open('playerdata.csv'))

    #open batting output file, or create if it doesn't exist
    output_file = open('Batting_Output.csv', 'a+')
    
    output_file.write('playernumber,singles,doubles,triples,homeruns,atbat,batavg,slugavg\n') #assign header to csv columns
    
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
        output_file.write('%s,%i,%i,%i,%i,%i,%.3f,%.3f\n' % (playernumber, singles, doubles, triples, homeruns, atbat, batavg, slugavg))
        
    output_file.close() #close output file

main()

