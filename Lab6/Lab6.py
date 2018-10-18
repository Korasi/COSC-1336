'''
This program prints parameters from restaurant data
Nigel Myers
Fundamentals of Programming
ACC FALL 2018
Lab6.py
Prof Onabajo
'''

class Restaurant:
    def __init__(self, data):
        #convert dict data into an object
        self.name = data['Restaurant Name']
        self.type = data['Food Type']
        self.reservations = True if data['Reservations'] == 'Yes' else False
        self.rating = int(data['Rating'])
        self.cards = True if data['Credit Cards'] == 'Yes' else False

'Header Data for this project: [ Restaurant Name, Food Type, Reservations, Rating, Credit Cards ]'

def parseCSV(filename, delimiter=','):
    # Usage: parseCSV(filename[, delimiter])
    with open(filename, 'r') as csv: #open file in read only
        csv_data = [] #init empty list
        header = csv.readline().strip('\n').split(delimiter) #split csv header by delim
        while True: #infinite loop
            row = csv.readline().strip('\n').split(delimiter) #split row by delim
            if len(row) == 1 and not row[0]: #if only one attribute in row, and row[0] is an empty string, treat as end of CSV
                return csv_data #return csv_data list 
            csv_data.append(Restaurant({header[iteration]:item for iteration, item in enumerate(row)})) #assign row as dict { header[item_index] : value for each item in row }

def nl():
    output('')

def output(string):
    global output_file
    print(string) 
    if output_file: #output to outfile only if specified
        output_file.write('%s\n' % string) 
    
def evaluate(restaurants, logic):
    for restaurant in restaurants: #loop through each restaurant object
        if eval(logic): #use parameter logic as a logical expression. 
            output(restaurant.name)
    nl()

def main():
    restaurants = parseCSV('Restaurants.csv') #open and parse Restaurants.csv
    with open('Lab6_Output.txt', 'w') as globals()['output_file']:
        #globals()['output_file'] = output
        
        output('Restaurants that accept credit cards:')
        evaluate(restaurants, 'restaurant.cards')

        output('Restaurants with >= 3 stars:')
        evaluate(restaurants, 'restaurant.rating >= 3')

        output('Chinese Restaurants with >= 3 stars:')
        evaluate(restaurants, 'restaurant.type == "Chinese" and restaurant.rating >=3')

        output('Restaurants with a 1-4 star rating:')
        evaluate(restaurants, 'restaurant.rating <= 4')
        
main()
