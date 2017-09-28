# Created by Joshua Schappel
# Built for Renew International

from bs4 import BeautifulSoup
import requests
import csv

# Array with all the states and places that are in the US
states = [' Alabama',' Alaska',' Arizona',' Arkansas',' California',' Colorado',
         ' Connecticut',' Delaware',' Florida',' Georgia',' Hawaii',' Idaho', 
         ' Illinois',' Indiana',' Iowa',' Kansas',' Kentucky',' Louisiana',
         ' Maine' ' Maryland',' Massachusetts',' Michigan',' Minnesota',
         ' Mississippi', ' Missouri',' Montana',' Nebraska',' Nevada',
         ' New Hampshire',' New Jersey',' New Mexico',' New York',
         ' North Carolina',' North Dakota',' Ohio',    
         ' Oklahoma',' Oregon',' Pennsylvania',' Rhode Island',
         ' South Carolina',' South Dakota',' Tennessee',' Texas',' Utah',
         ' Vermont',' Virginia',' Washington',' West Virginia',
         ' Wisconsin',' Wyoming', ' (Melkite Greek)', ' District of Columbia'
         ]
titleList = ['Bishop', 'Archbishop']

# List for the data to be stored in
locationList = list()
nameList = list()
extensionList = list()
titleLocationList = list()


i = 0
while i < 3:

    # Get the page
    if i == 0:
        page = requests.get("http://www.catholic-hierarchy.org/country/bus2.html")
        soup = BeautifulSoup(page.content, 'lxml')
    elif i == 1:
        page = requests.get("http://www.catholic-hierarchy.org/country/bus2b.html")
        soup = BeautifulSoup(page.content, 'lxml')
    else:
        page = requests.get("http://www.catholic-hierarchy.org/country/bus2c.html")
        soup = BeautifulSoup(page.content, 'lxml')

    # Since there are many ul tags we will find the child of the tag we want and then go to its parent
    ul = soup.find('br').parent.find_all('li')
    i = i + 1
    
    # Loop that will find and sort the data
    for li in ul:
        
        data =(li.get_text(strip=False))
        data = data.split(",")

        # Data cleanup     
        if "\n\n\n" in data[-1]:
            data[-1] = data[-1].replace("\n\n\n", "")
        elif "\r\n" in data[-1]:
            data[-1] = data[-1].replace("\r\n", "")
        elif "\n" in data[-1]:
            data[-1] = data[-1].replace("\n", "")
        elif "\r" in data[-1]:
            data[-1] = data[-1].replace("\r","")
        else:
            break  

        # Get the state
        # This will be our main sorter since it will remove any places that are not in the USA
        if any(word in data[-1] for word in states):

            if len(data) > 2: #If it is 2 or less state is not provided
                locationList.extend([data[-1]])

            # Special cases
            if len(data) == 4:
                extensionList.extend([data[1]])
                titleLocationList.extend([data[2]])
            elif len(data) == 3: # This is the normal case (no extension)
                titleLocationList.extend([data[1]])
                extensionList.extend(" ")
            elif len(data) == 5: # Not sure yet if this case is possiable
                print("found you")
            else: # Must be the len = 2 case, Mabye make this the 3 case?
                extensionList.extend(" ")
                locationList.extend(" ")
                titleLocationList.extend([data[1]])
                
            # Get full name and title
            # Remove title because its already in the next column
            if "Bishop" in data[0]:
                data[0] = data[0].replace("Bishop ","")
                nameList.extend([data[0]])
            elif "Archbishop" in data[0]:
                data[0] = data[0].replace("Archbishop ","")
                nameList.extend([data[0]])
            else:
                nameList.extend([data[0]])
                
# Zip the list up into a tuple
zipList = zip(nameList,titleLocationList,extensionList,locationList)

# write the zipList to a cvs file
with open('BishopList.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in zipList:
        writer.writerow(row)
print("The program is now finished. Please open excel file titled: Bishop List")
