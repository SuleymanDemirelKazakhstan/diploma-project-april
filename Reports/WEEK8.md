# Arailym Abdrakhym
*    In the 8th week Arailym organized meetings with the members and mentor, and talked about the project and its progress,proof is below:
      + [Youtube](https://youtu.be/Kwo2YrUfA48)

*   Also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants of group do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.52.05.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.50.57.png)
*          Parsing data from IEEE Xplore using Python:
   * learned scraping of IEEE Xplor
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2006.15.43.png)
       + Coding part
````py
import requests
import json
import csv    #Ieeexplore parsing code


FILE = 'publications.csv'

def iexplore(querytext):
    url_base = 'https://ieeexplore.ieee.org'
    url = url_base + "/rest/search"


    payload = json.dumps({
      "newsearch": True,
      "queryText": querytext,
      "highlight": True,
      "returnFacets": [
        "ALL"
      ],
      "returnType": "SEARCH",
      "matchPubs": True
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Origin': 'https://ieeexplore.ieee.org',
      'Cookie': 'JSESSIONID=1f1uodkJQyFydS1nj60dhUga9TzcL1eSS2GtBmSb4I2UWoFyct4e!-1059566563; TS01b03060=012f3506239362e2457f97d2093c7ee2a7ae609257d4f289c6faeaf1e87e8b729d50e85168a48a955b71aa49179c7761b2b63e68b1; WLSESSION=203580044.20480.0000; ipCheck=46.34.147.74'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    out = json.loads(response.text)

    for rec in out['records']:
        for au in rec['authors']:
            print(au['normalizedName'])  # фио authors
        print('highlightedTitle:  ' + rec['highlightedTitle']) #title
        print('htmlLink:  ' + url_base + rec['htmlLink'])  #link
        print('publicationYear:  ' + rec['publicationYear'])  #year
        print('publisher:  ' + rec['publisher']) #publisher
        print('publicationTitle:  ' + rec['publicationTitle'])
        print('displayContentType:  ' + rec['displayContentType']) #content type
        print(rec['startPage'] + ' - ' + rec['endPage'])
        print('pdfSize:  ' + rec['pdfSize']) #size
        print('--------------')
    with open(FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['IEEE Xplore'])
        writer.writerow([ 'Title', 'HtmlLink', 'Place of publications', 'Publisher', 'Date', 'Pages'])
        for item in out['records']:
            print("Ждите")
            writer.writerow([
                item['highlightedTitle'], #title
                item['htmlLink'], #link
                item['displayContentType'],#place
                item['publisher'], #publisher
                item['publicationDate'], #date
                item['pdfSize']])  #pages


iexplore("olimzhon")


````
    

# Albina Niyetullayeva
* Design confirmation from the team and upgrade all files.  improving existing design (Figma)
  
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:23.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:27.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:33.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:30.jpg)
  
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:35.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:25.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:38.jpg)
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:41.jpg)
   * New Logo
   * ![new logo](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2006:21:17.jpg)
   
 
# Aruzhan Kutzhan

* Data analysis & research 
   + ![]()

# Shynar Toktar
*      Parsing data from IEEE Xplore using Python
    + Coding part
````py
def iexplore(querytext):
    url_base = 'https://ieeexplore.ieee.org'
    url = url_base + "/rest/search"


    payload = json.dumps({
      "newsearch": True,
      "queryText": querytext,
      "highlight": True,
      "returnFacets": [
        "ALL"
      ],
      "returnType": "SEARCH",
      "matchPubs": True
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'en-US,en;q=0.9',
      'Origin': 'https://ieeexplore.ieee.org',
      'Cookie': 'JSESSIONID=1f1uodkJQyFydS1nj60dhUga9TzcL1eSS2GtBmSb4I2UWoFyct4e!-1059566563; TS01b03060=012f3506239362e2457f97d2093c7ee2a7ae609257d4f289c6faeaf1e87e8b729d50e85168a48a955b71aa49179c7761b2b63e68b1; WLSESSION=203580044.20480.0000; ipCheck=46.34.147.74'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    out = json.loads(response.text)

````
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2014.32.09.png)
