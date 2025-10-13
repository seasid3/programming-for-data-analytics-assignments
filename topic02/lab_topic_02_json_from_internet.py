# Import json from internet
# Author: Andrew Beatty from lab and Orla Woods comments added

'''

import requests  # requests library to handle http requests
url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) # name the request function as response
data = response.json() # define database using json
print(data) 
# the output is a dictionary (all the curly brackets) with keys (bank-holidays, england-and-wales, scotland, northern-ireland)
# and values (the rest of the information)
'''


import requests  # requests library to handle http requests
url =" https://www.gov.uk/bank-holidays.json" 
response = requests.get(url) # name the request function as response
data = response.json() # define database using json
print(data['northern-ireland']['events'][0])  # modify to output the first event only in 
# northern-ireland (index 0)


