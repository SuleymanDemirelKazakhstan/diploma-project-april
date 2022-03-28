from turtle import title
import requests
from bs4 import BeautifulSoup
import time


def pubmed(lastname, name = None):
    result = []

    url = "https://pubmed.ncbi.nlm.nih.gov/?term="+lastname
    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    items = soup.find_all("div", class_="docsum-content")
    i = 1
    for item in items:
        reslist = {}
        reslist["Site"] = "Pubmed" + str(i)
        i += 1
        reslist['Authors'] = item.find("span", class_="docsum-authors full-authors").get_text()
        reslist["Title"] = item.find("a",class_="docsum-title"). get_text() # title
        reslist['Link'] =  'https://pubmed.ncbi.nlm.nih.gov/' + item.find("a", class_="docsum-title").get("href")  # link
        wh = item.find("span", class_="docsum-journal-citation full-journal-citation").get_text()
        reslist['Year'] = wh[(wh.find(".") + 2 ):wh.find(";",)]  # year
        reslist['Publisher']  = item.find("span", class_="docsum-journal-citation short-journal-citation").get_text()  # publisher

        reslist['Where published'] = wh[:wh.find(".")]
        reslist["PP."] = wh[(wh.find(")") + 1):wh.find(".", wh.find(".") + 1)]
        result.append(reslist)
    return result

