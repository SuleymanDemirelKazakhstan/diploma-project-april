# Arailym Abdrakhym
*   As PM, in the 6th week I organized meetings with the members and with the mentor, and talked about the project and its progress,proof is below:
    + [Youtube](https://www.youtube.com/watch?v=uv_URQlW_jg)

*   I also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2000.22.48.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2000.23.28.png)
*  Scraping [Scopus](https://www.scopus.com/home.uri):
    + before starting to write code, I with Shynar analyzed the site itself, which will be parsed, studied the code of this site, and then proceeded to the questions:"How will it parse?"
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-10%20в%2014.31.41.png)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-10%20в%2014.31.46.png)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-12%20в%2002.07.22.png)
     + I searched for an easy way of Parsing and came across several python libraries, initially she thought that she would use only bs4.BeautifulSoup
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2001.57.08.png)
       + I tried to launch several variants with code changes, the site blocked, and did not give information, and displayed only an empty list, then she used json, there were also errors in the code, and plus my partner - Shynar at that time considered another option using the API, then I also studied parsing methods with her using the API...
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2001.40.36.png)
*  
   *  Coding part
      + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.05.58.png)
      + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.08.08.png)
      + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.06.24.png)
      + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.06.27.png)
      + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-14%20в%2004.06.30.png)
      + Exception: Error: The requestor is not authorized to access the requested view or fields of the resource url...

# Albina Niyetullayeva
* Website structure design, main elements of the site: Registration page, Help page, About us page
    * Made design of Register page
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2002:25:13.jpg)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2002:25:15.jpg)
   * Help page
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2002:25:36.jpg)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2002:25:41.jpg)
   * About us page
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2002:25:46.jpg)
   * Logo
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2003:51:56.jpg)
# Aruzhan Kutzhan

* Data analysis & research []()

# Shynar Toktar
* Learned: Python based Scopus Api  
  + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2004:30:11.jpg)
    
    + In the study of parsing, I realized that the functions and algorithms of parsing for each site will be separate, because the structure and protective functions of each site are different. We started the process of parsing sites from the Scopus site. You can parse SCOPUS using several options. And we started the parsing process with the Scopus api.
  * Coding part
    
````py
import requests
import json
import csv
from pybliometrics.scopus import AuthorSearch

MY_API_KEY = '16d73d54a99ebb00d7c13b6d00fe2fb1'

def author_search(scopus_id, count_increment=20,start_offset=0):

    headers = { 'Accept':'application/json',
                'X-ELS-APIKey': MY_API_KEY }
    co_authors ="https://api.elsevier.com/content/search/author"
    params = {
        'co-author' : scopus_id,
        'count': count_increment,
        'start': start_offset,
        'field': 'dc:identifier,preferred-name,affiliation-current'}
    result = requests.get(url=co_authors, params=params,headers=headers).json()
    return result
#author_search('55832104800')

def author_search():
    resp = requests.request("POST", "http://api.elsevier.com/content/author?author_id=7004212771&view=metrics",
                        headers={'Accept': 'application/json',
                                 'X-ELS-APIKey': MY_API_KEY})
    out = json.loads(resp.text)
    print(out)

    print(json.dumps(resp.json(),
               sort_keys=True,
               indent=4, separators=(',', ': ')))

#author_search()
````
  
*
    + Access to documents is controlled using a combination of API Key and A&E authorization rights. Even if the APIKey is correctly configured for access, the account does not contain sufficient access rights. We paused work with the API because we did not get the data. Since our account does not have enough rights. After that, we started writing parsing code in parallel, which should work without API.
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2011:50:33.jpg)

* Scopus scraping without API
     + We used the requests and BeautifulSoup libraries to get data from a web page. 

````py
import json
import requests
from bs4 import BeautifulSoup
import time

URL = "https://www.scopus.com/results/authorNamesList.uri?st1=Baimuratov&st2=o&origin=searchauthorlookup"

def get_html(url, params=None):
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "accept": "*/*",
        'Content-Type': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'https://www.scopus.com'}

    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_url(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all("td", class_="authorResultsNamesCol")
    for item in items:
            id = item.find("a",class_="docTitle").get("href")
    return 'https://www.scopus.com/' + id

def get_content(html):
    soup = BeautifulSoup(html,"html.parser")
    print(soup)
    print('sleep start')
    time.sleep(30)
    print('sleep end')
    items = soup.find_all("li", class_="results-list-item")
    print(items)
    #for item in items:
     #       print(item.find("div",class_="list-title margin-size-24-t margin-size-0-b text-width-32").get_text())

def parse():
    #pass
    html = get_html(URL)
    if html.status_code==200:
        url = get_url(html.text)
        print(url)
        html1 = get_html(url)
        if html1.status_code==200:
            get_content(html1.text)
        else:
            print('Error html1')
    else:
        print("Error")
parse()

````
* We have completed the search part. With the author's surname and first name, we can find his Scopus id. And with ID, we go to the page where all his publications are located. Due to a problem with access, we get an empty sheet.
     + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-03-14%2012:13:51.jpg) 
