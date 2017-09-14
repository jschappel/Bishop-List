from bs4 import BeautifulSoup
import requests
import csv


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


title = ''
firstName = ''
lastName = ''
middleName = ''

myList = list()




# Get the page
page = requests.get("http://www.catholic-hierarchy.org/country/bus2.html")
soup = BeautifulSoup(page.content, 'lxml')

# Since there are many ul tags we will find the child of the tag we want and then go to its parent
ul = soup.find('br').parent.find_all('li')

b = open('player2.csv','a')
a = csv.writer(b)

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
    #print (data[0])    

    # Get the state
    # This will be our main sorter since it will remove any places that are not in the USA
    if any(word in data[-1] for word in states):
      #  print (data[-1])
        myList.extend(data)
        list2 = list()
        list2.extend([data[-1]])
        
        #print(list2)

        #Get full name and title
        nameList = list()
        nameList.extend([data[0]])
        #print(nameList)
        a.writerows([nameList])
        a.writerows([list2])

        


#print (len(myList))
#print(list2)

b.close()   
#print(myList)
    
