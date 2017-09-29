# Bishop List
### Overview

This program uses the website [Catholic Hierarchy](http://www.catholic-hierarchy.org/) to create an Excel spreadsheet of all the living bishops in the USA (not including USA territories). Below is an example of the format:

First Middle Last | Title and City | Other Special Titles (if needed) | State |
------------ | ------------- | -------------| -------------
Joseph Victor Adamec |  Bishop Emeritus of Altoona-Johnstown | |  Pennsylvania
Emilio Simeon Alluè |  Auxiliary Bishop Emeritus of Boston | S.D.B. |  Massachusetts



### Built with:
* [Beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/) - Used for web scrapping
* [CSV](https://docs.python.org/3/library/csv.html) - Used to write to CSV file
* [Requests](https://pypi.python.org/pypi/requests/2.12.1) - Used to get the webpage


### Download Instructions:
##### For Mac
1. Download the latest version of [Python 3](https://www.python.org/downloads/)
2. In Finder under Applications click on terminal
3. Type the following:
   * sudo pip3 install beautifulsoup4
   * sudo pip3 install requests
  
##### For Windows
1. Download the latest version of [Python 3](https://www.python.org/downloads/).
2. Open your Python folder in file explorer. An easy way to do this is to search for *Python* in *This PC* search bar.
3. Locate the scripts folder, then hold shift + right click. Then select *Open command line here*
4. In the command line type the following:
   - pip install requests
   - pip install beautifulsoup4

### Deployment:
##### For Windows Only
To run the program double click on the *Bishop.py* file. You can also choose to run the program through IDLE. To do this right click the *Bishop.py* file and under *open with* select *Python*. If Python does not show up right away select *choose another app* then search and select Python.
##### For Mac and Windows
To run the program right click on the *Bishop.py* file and under run with (In Windows it’s called "Edit With") select *IDLE*. Then press fn + F5 to run the program (On Windows you just need to press f5).


* Once the program has run it will create a csv file titled **BishopList.csv** that is saved to the same location as the program.
* You are now free to open the program in Google Docs, Pages or any program that offers UTF-8 support.

**If you plan to run this program in Excel please do the following:**
1. Open Excel
2. Select the "Data" tab
3. Select "Get External Data"
4. Select "From Text" and open BishopList.csv
5. On the first window that appears, under File Origin select "Unicode: (UTF-8)"
   - Depending on your version of Excel the file origin name might differ. Any option containing "UTF-8" should work.
7. Under Original Data Type select "Delimited"
8. Click "Next"
9. Under Delimiters, deselect "Tab" and select "Comma"
10. Click "Next"
11. Under Column Data Format select "general"
12. Then click "Finish"
13. On the last window choose whether you want it to appear on a new sheet or not and then click "Finish"
    
 **If the above was confusing see these [instructions](https://www.itg.ias.edu/content/how-import-csv-file-uses-utf-8-character-encoding-0). Note: These instructions will work for all versions of Excel.**

### Author
Joshua Schappel - *Creator* - [JSchappel](https://github.com/jschappel)
