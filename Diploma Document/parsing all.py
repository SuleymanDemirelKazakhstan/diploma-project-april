from doaj import *
from pubmed import *
from GoogleScholar import *
from ieeexplore import *
import csv    #parsing all

def parsing(lastname, name):
    FILE = 'publications.csv'

    lastname = "Baimuratov"
    name = "O"

    l_doaj = doaj(lastname, name)
    l_pubmed = pubmed(lastname, name)
    l_scholar = googlescholar(lastname, name)
    l_iexplore = iexplore(lastname, name)
    all = l_doaj + l_pubmed + l_scholar + l_iexplore

    with open(FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Site','Title', 'HtmlLink', 'Authors', 'Publisher', 'Date', 'Pages'])
        for item in l_scholar+l_iexplore:
            print("Ждите")
            writer.writerow([
                item['Site'],
                item['Title'],  # title
                item['Link'],  # link
                item['Authors'],  # place
                item['Publisher'],  # publisher
                item['Year'],  # date
                item['PP.']])  # pages

parsing("baimuratov", "O")