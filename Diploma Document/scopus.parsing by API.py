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
