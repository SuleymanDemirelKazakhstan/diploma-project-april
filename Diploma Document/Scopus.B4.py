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
