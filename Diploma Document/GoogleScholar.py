import requests
from bs4 import BeautifulSoup
import time
import csv    #Google scholar parsing code

FILE = 'publications.csv'

URL = "https://scholar.google.com/scholar?hl=ru&as_sdt=0%2C5&q=baimuratov+o"

def get_html(url, params=None):
    HEADERS = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "accept": "text/html, */*"}

    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_url(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("h4", class_="gs_rt2")
    for item in items:
            html1 = item.find("a", class_=None).get("href")
    return 'https://scholar.google.com/' + html1

def get_content(html, url):
    soup = BeautifulSoup(html,"html.parser")
    print('sleep start')
    time.sleep(1)
    print('sleep end')
    '''
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_id('gsc_bpf_more')
    button.click()
    '''
    items = soup.find_all("tr", class_="gsc_a_tr")
    for item in items:
        print('Title: ' + item.find("a",class_="gsc_a_at").get_text())
        print('Link: ' + 'https://scholar.google.com/' + item.find("a", class_="gsc_a_at").get("href"))
        print('Authors: ' + item.find("div", class_="gs_gray").get_text())
        print('Publisher: ' + item.find("div", class_="gs_gray").find_next("div").get_text().rsplit(',', 1)[0])
        print('Year: ' + item.find("span", class_="gsc_a_h gsc_a_hc gs_ibl").get_text())
        print('---------------------')

    with open(FILE, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Google Scholar'])
        writer.writerow([ 'Title', 'HtmlLink', 'Place of publications', 'Publisher', 'Date', 'Pages'])
        for item in items:
            print("Ждите")
            writer.writerow([
                item.find("a",class_="gsc_a_at").get_text(), #title
                'https://scholar.google.com/' + item.find("a", class_="gsc_a_at").get("href"), #link
                'Google scholar',#place
                item.find("div", class_="gs_gray").find_next("div").get_text().rsplit(',', 1)[0], #publisher
                item.find("span", class_="gsc_a_h gsc_a_hc gs_ibl").get_text(), #date
                item.find("div", class_="gs_gray").find_next("div").get_text().rsplit(',', 2)[1]])  #pages
def parse():
    #pass
    html = get_html(URL)
    if html.status_code==200:
        url = get_url(html.text)

        html1 = get_html(url)
        if html1.status_code==200:
            get_content(html1.text, url)
        else:
            print('Error html1')
    else:
       print("Error")
parse()



