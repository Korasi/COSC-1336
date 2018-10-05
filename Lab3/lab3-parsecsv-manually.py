# This program computes batting and slugging averages from a given csv file of player data.
# Nigel Myers
# Fundamentals of Programming
# ACC FALL 2018
# lab3-parsecsv-manually.py
# Prof Onabajo

# Version: import .csv; output .txt

#parse csv function
def parseCSV(filename, delimiter=','):
    # Usage: parseCSV(filename[, delimiter])
    with open(filename, 'r') as csv: #open file in read only
        csv_data = [] #init empty list
        header = csv.readline().strip('\n').split(delimiter) #split csv header by delim
        while True: #infinite loop
            row = csv.readline().strip('\n').split(delimiter) #split row by delim
            if len(row) == 1 and not row[0]: #if only one attribute in row, and row[0] is an empty string, treat as end of CSV
                return csv_data #return csv_data list 
            csv_data.append({header[iteration]:item for iteration, item in enumerate(row)}) #assign row as dict { header[item_index] : value for each item in row }

def output(string, outfile=None):
    print(string) 
    if outfile: #output to outfile only if specified
        outfile.write('%s\n' % string) 

def main():
    players = parseCSV('playerdata.csv') #open and parse playerdata.csv

    #open batting output file, or create if it doesn't exist
    with open('Batting_Output_Formatted.txt', 'w') as output_file:
        output('%7s | %7s | %7s | %7s | %9s | %6s | %6s | %6s |' % ('Player', 'Singles', 'Doubles', 'Triples', 'Home Runs', 'At Bat', 'BAVG', 'SLGAVG'), output_file) #assign header to output
        for player in players: #repeat section for each row in CSV
            #Assign variables for each value in dict player from list players
            player_ = player['playernumber']
            singles = int(player['singles'])
            doubles = int(player['doubles'])
            triples = int(player['triples'])
            homeruns = int(player['homeruns'])
            atbat = int(player['atbat'])

            #Calculate Batting and Slugging averages
            batavg = (singles + doubles + triples + homeruns) / atbat
            slugavg = (singles + doubles * 2 + triples * 3 + homeruns * 4) / atbat #multiply double/triple/hr by base value
            
            #print all data and export to outputfile
            output('%7s | %7s | %7s | %7s | %9s | %6s | %6.3f | %6.3f |' % (player_, singles, doubles, triples, homeruns, atbat, batavg, slugavg), output_file)

main()
