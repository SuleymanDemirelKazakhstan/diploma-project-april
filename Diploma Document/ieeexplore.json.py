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


