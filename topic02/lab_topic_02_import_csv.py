# Input csv and output as list
# Author: Andrew Beatty from lab and Orla Woods comments added

import csv

FILENAME= "data.csv" 
DATADIR = "../topic02/"

'''
# open the csv, read as text. fp is the new name as the file. print line by line, as a list.
# 
# with open (DATADIR + FILENAME, "rt") as fp: 
    reader = csv.reader(fp, delimiter=",") 
    for line in reader:        
        print (line) 
'''

'''

# open the csv, read as text. fp is the new name as the file. print line by line, as a list. 
# output is a list of strings separated by lines between each row
with open (DATADIR + FILENAME, "rt") as fp:
         reader = csv.reader(fp, delimiter=",")
         linecount = 0     
         for line in reader:         
            if not linecount: # first row ie header row            
                 print (f"{line}\n-------------------")        
            else: # all subsequent rows             
                print (line)         
                linecount += 1 

'''

'''

with open (DATADIR + FILENAME, "rt") as fp:     
    reader = csv.reader(fp, delimiter=",")     
    linecount = 0     
    total = 0     
    for line in reader:         
        if not linecount: # first row ie header row 
            pass         
        else: # all subsequent rows             
            total += int(line[1]) # why 1 - because index 0 is the header
        linecount += 1    
    print (f"average is {total/(linecount-1)}") # why -1 ? - beacuse the header row is not counted
    # for average calculation 
'''

'''
with open (DATADIR + FILENAME, "rt") as fp:    
     reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)     
     linecount = 0     
     total = 0     
     for line in reader:        
        if not linecount: # first row ie header row 
            pass         
        else: # all subsequent rows             
            total += line[1] # why 1          
    
        linecount += 1    
     print (f"average is {total/(linecount-1)}") # why -1 ? 
'''

# use dictreader to read the csv as a dictionary
with open (DATADIR + FILENAME, "rt") as fp:     
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)     
    total = 0     
    count = 0     
    for line in reader:         
        total += line['age']     
        # print (line)         
        count +=1    
    print (f"average is {total/(count)}") # why is there no -1 this time? - because the header row
    # is not counted in the dictreader. The "names" of the column headers are used as the keys
    # in the imported dictionary. 