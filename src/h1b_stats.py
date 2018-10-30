#this script calculates top 10 occupations and states for certified H1B visa
#application with data from the OFCPD and outputs the data as text files

#import modules
import os
import sys
import csv
from collections import Counter

#function to read data from csv file
def read_csv(filename):
    """Read csv file and return data as m nested lists of length n, with m the
    number of rows and n the number of columns in the csv file."""
    
    #list where content of csv file is stored
    data = []
    
    #read file and append list
    path = os.path.join('./input/', filename)
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            data.append(row)
            
    #first element of first nested list is represent row numbers
    data[0][0] = 'row_number'
    
    return data

#function to get top occupation
def get_top_occupations(data, top, output_name):
    """Function which get top occupations from data along with number and
    percentage of certified applications, then saves results as a text file. 
    By default, returns top 10 occupations."""
    
    #get column names
    col_names = data[0]
    #for name in data[0]:
    #    col_names.append(name)
    
    #get index for status and occupation name
    for i in range(len(col_names)):
        if 'STATUS' in col_names[i]:
            status_index = i
        if 'SOC_NAME' in col_names[i]:
            soc_index = i
    
    #for each application put occupation in list if status is certified
    soc_codes = []
    #remember first row is column names
    for i in range(1, len(data)):
        if data[i][status_index] == 'CERTIFIED':
            soc_codes.append(data[i][soc_index])
    
    #count number of each occupation and rank them
    c = Counter(soc_codes)
    top_10_occup = c.most_common(top)
    
    #sort top 10 occupations by number then name if there are ties
    top_10_occup.sort(key=lambda x: x[0])
    top_10_occup.sort(key=lambda x: x[1], reverse=True)
    
    #total number of certified applications for percentage calculation
    total_certif = sum(c.values())
    
    #write data in csv file
    path = os.path.join('./output/', output_name)
    with open(path, 'w') as txtfile:
        writer = csv.writer(txtfile, delimiter=';')
        writer.writerow(['TOP_OCCUPATIONS', 
                         'NUMBER_CERTIFIED_APPLICATIONS', 
                         'PERCENTAGE'])
        for row in top_10_occup:
            writer.writerow([row[0], 
                             row[1], 
                             str(round(row[1]/total_certif, 1) * 100) + '%'])
    
    return top_10_occup
  
#function to get top states
def get_top_states(data, top, output_name):
    """Function which get top states from data along with number and
    percentage of certified applications, then saves results as a text file."""
    
    #get column names
    col_names = data[0]
    #for name in data[0]:
    #    col_names.append(name)
    
    #get index for status and state name
    #different years have different column names
    for i in range(len(col_names)):
        if 'STATUS' in col_names[i]:
            status_index = i
        if 'WORKSITE_STATE' in col_names[i]:
            state_index = i
        if 'WORKLOC1_STATE' in col_names[i]:
            state_index = i
    
    #for each application put state in list if status is certified
    states = []
    #remember first row is column names
    for i in range(1, len(data)):
        if data[i][status_index] == 'CERTIFIED':
            states.append(data[i][state_index])
    
    #count number of each occupation and rank them
    c = Counter(states)
    top_10_states = c.most_common(top)
    
    #sort top 10 occupations by number then name if there are ties
    top_10_states.sort(key=lambda x: x[0])
    top_10_states.sort(key=lambda x: x[1], reverse=True)
    
    #total number of certified applications for percentage calculation
    total_certif = sum(c.values())
    
    #write data in csv file
    path = os.path.join('./output/', output_name)
    with open(path, 'w') as txtfile:
        writer = csv.writer(txtfile, delimiter=';')
        writer.writerow(['TOP_STATES', 
                         'NUMBER_CERTIFIED_APPLICATIONS', 
                         'PERCENTAGE'])
        for row in top_10_states:
            writer.writerow([row[0], 
                             row[1], 
                             str(round(row[1]/total_certif, 1) * 100) + '%'])
    
    return top_10_states


if __name__ == '__main__':
    
    #get input and output file names
    filename = sys.argv[1]
    output_occup = sys.argv[2]
    output_state = sys.argv[3]
    
    #read csv file
    data = read_csv(filename)
    
    #use dummy variable for functions, we are interested in output files
    _ = get_top_occupations(data, 10, output_occup)
    _ = get_top_states(data, 10, output_state)