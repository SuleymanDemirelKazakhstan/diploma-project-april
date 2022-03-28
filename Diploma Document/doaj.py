import requests
import json  # doaj parsing code end
def doaj(lastname, name):
    result = []
    headers = {"Accept": "application/json"}
    url = 'https://doaj.org/api/search/articles/' + lastname + '%20' + name
    r = requests.get(url, headers=headers)
    res = json.loads(r.text)
    i = 1
    for rec in res['results']:
        reslist = {}
        aut = []
        for au in rec['bibjson']['author']:
            aut.append(au['name'])
        reslist["Site"] = "DOAJ" + str(i)
        i += 1
        reslist['Authors'] = ",".join(aut)
        reslist["Title"] = rec['bibjson']['title'] # title
        reslist['Link'] =  rec['bibjson']['link'][0]['url']  # link
        reslist['Year']= rec['bibjson']['year']  # year
        reslist['Publisher']  = rec['bibjson']['journal']['publisher']  # publisher
        reslist['Where published'] = rec['bibjson']['journal']['title']
       # print('displayContentType:  ' + rec['displayContentType'])  # content type
        reslist['PP.'] = rec['bibjson']['start_page'] + ' - ' + rec['bibjson']['end_page']
        reslist['Volume'] = rec['bibjson']['journal']['volume']
        reslist['Number'] = rec['bibjson']['journal']['number']  # size
        result.append(reslist)

    return result




