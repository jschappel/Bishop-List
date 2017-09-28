# Bishop-List
### Overview

This program uses the website, [Catholic Hierarchy](http://www.catholic-hierarchy.org/), to create an excel spreadsheet of all the living bishops in the USA (not including USA Territories). Below is an example of the format:

First Middle Last | Title and City | Other Special Titles (if needed) | State |
------------ | ------------- | -------------| -------------
Joseph Victor Adamec |  Bishop Emeritus of Altoona-Johnstown | |  Pennsylvania
Emilio Simeon Alluè |  Auxiliary Bishop Emeritus of Boston | S.D.B. |  Massachusetts



### Built with:
* [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - Used for web scrapping
* [CSV](https://docs.python.org/3/library/csv.html) - Used to write to CSV file
* [Requests](https://pypi.python.org/pypi/requests/2.12.1) - Used to get the webpage


### Download Instructions
##### For Mac
1. Downlaod the latest version of [Python 3](https://www.python.org/downloads/)
2. In Finder under Applications click on terminal
3. type the following:
   * sudo pip3 install beautifulsoup4
   * sudo pip3 install requests
  
##### For Windows
1. Downlaod the latest version of [Python 3](https://www.python.org/downloads/).
2. Open your python folder in file explorer. An easy way to do this is to search for *Python* in *This PC* search bar.
3. Locate the scripts folder, then hold shift + right click. Then select *Open command line here*
4. In the command line type the following:
   - pip install requests
   - pip inastll beautifulsoup4
  
### Deployment
To run the program double click on the *Bishop.py* file. You can also choose to run the program through IDLE. to do this right click the *Bishop.py* file and under *run with* select *choose another file* then search and select IDLE. Once the program has run it will create a csv file titled **BishopList.csv** that is saved to the same location as the program. You can open the file by right clicking on it and selecting Excel.

### Special Instructions for Opening the file with Mac Excel
If you are running this program on a Mac it is recommended for you to use Pages because Mac excel does not support utf-8 encoding. If you choose to use excel, see these [instructions](https://www.itg.ias.edu/content/how-import-csv-file-uses-utf-8-character-encoding-0).

### Author
Joshua Schappel - *Creator* - [JSchappel](https://github.com/jschappel)
