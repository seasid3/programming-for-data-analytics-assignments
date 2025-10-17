# Thiis program prints out the bank holidays in Northern Ireland
# Author: Orla Woods

import requests  # requests library to handle http requests
url ="https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) # name the request function as response
data = response.json() # define database using json

# sanity check on the import
# print(data) 

# using code from the lab. Print only data for Northern Ireland

# print(data['northern-ireland']['events'])  

# Last few marks: modify the program to print the bank holidays that are unique to Northern Ireland.

# using copilot code which is trying to look at the wrong part of the dataset, so modifying it, along
# with code from the lab
ni_holidays = data['northern-ireland']['events'] # define ni_holidays as the events in northern ireland
# not from co-pilot but i knew i needed to define the events in england and wales and scotland
# so i can say if "x is not in y"
other_holidays = data['england-and-wales']['events'] + data['scotland']['events']

# initial code was close but not there so i asked chatgpt for help:
# https://chatgpt.com/share/68edffac-fbf4-800d-bc10-a69b4dbdd52e
# I hadn't realised I should access the list of all other holidays first
# access all other UK holiday titles for comparison
other_titles = [holiday['title'] for holiday in other_holidays]

# identify holidays unique to Northern Ireland
unique_ni_holidays = [holiday for holiday in ni_holidays if holiday['title'] not in other_titles]

# print output
for holiday in unique_ni_holidays:
    print(f"{holiday['title']} is a holiday unique to Northern Ireland and it takes place on {holiday['date']}") 