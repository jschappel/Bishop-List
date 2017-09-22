from bs4 import BeautifulSoup
import requests
import csv

# Array with all the states and places that are concidered in the US
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

# List for the data to be stored in
myList = list()
list2 = list()
nameList = list()
extensionList = list()
titleLocationList = list()


# Get the page
page = requests.get("http://www.catholic-hierarchy.org/country/bus2.html")
soup = BeautifulSoup(page.content, 'lxml')

# Since there are many ul tags we will find the child of the tag we want and then go to its parent
ul = soup.find('br').parent.find_all('li')


i = 0
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
        myList.extend(data)

        if len(data) > 2: #If it is 2 or less state is not provided
            list2.extend([data[-1].encode('utf-8')])
        
        #print(len(data))

        # Special cases
        if len(data) == 4:
            extensionList.extend([data[1].encode('utf-8')])
            titleLocationList.extend([data[2].encode('utf-8')])
        elif len(data) == 3: # This is the normal case (no extension)
            titleLocationList.extend([data[1].encode('utf-8')])
            extensionList.extend(" ")
        elif len(data) == 5: # Not sure yet if this case is possiable
            print("found you")
        else: # Must be the len = 2 case, Mabye make this the 3 case?
            extensionList.extend(" ")
            list2.extend(" ")
            titleLocationList.extend([data[1].encode('utf-8')])

            
        #Get full name and title
        #nameList = list()
        nameList.extend([data[0].encode('utf-8')])
        #print(nameList)
        #a.writerows([nameList])
        #a.writerows([list2])

# Zip the list up into a tuple

#writer = csv.DictWriter(output, fieldnames=['date', 'v'])


# Create the csv file to write data to
#b = open('BishopSheet.csv','a')
#a = csv.writer(b)

zipList = zip(nameList,titleLocationList,extensionList,list2)
#decodedZipList = [[word.decode("utf-8") for word in sets] for sets in zipList]


#print(nameList)
with open('BishopList.csv', 'a', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in zipList:
        writer.writerow(row)
print("all done")
#for row in rows:
#    print(row)
#    a.writerow([row])
#print (len(myList))
#print(list2)

# Close out of the writer
#b.close()   
#print(myList)
    
