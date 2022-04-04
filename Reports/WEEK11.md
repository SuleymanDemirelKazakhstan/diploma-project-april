# Arailym Abdrakhym
*    In the 11th week Arailym organized meetings with the members and mentor, and talked about the project and its progress,proof is below:
      + [Youtube](https://youtu.be/P1cDPUIgxtI)

*   Also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants of group do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/11.pm.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/11.pm.1.png)

   * Learned python's library Matplotlib
       + Plotting graphs and histograms
       + Data analysis using the graphical method
       + Working with dates (updating the schedule in real time)
       + Working with the Seaborn library
       + [https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/](https://devpractice.ru/matplotlib-lesson-1-quick-start-guide/)
       + [https://python-scripts.com/matplotlib](https://python-scripts.com/matplotlib)
      

# Albina Niyetullayeva
* Learned Formspree
  
   * is a form backend, API, and email service for HTML & JavaScript forms. It's the simplest way to embed custom contact us forms, order forms.
# Aruzhan Kutzhan

* Going to filter and displays the final result on the website


# Shynar Toktar
*      Parsing data from Scopus using Python
    + Coding part
    + [API Call: https://api.elsevier.com/content/search/index:SCOPUS?query=AUTHLASTNAME(olimzhon)&apikey=16d73d54a99ebb00d7c13b6d00fe2fb1](https://api.elsevier.com/content/search/index:SCOPUS?query=AUTHLASTNAME(olimzhon)&apikey=16d73d54a99ebb00d7c13b6d00fe2fb1)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-04-04%2014:38:02.jpg)
    + Coding part
````py

from pybliometrics.scopus import ScopusSearch
from pybliometrics.scopus import AuthorRetrieval
from pybliometrics.scopus import AuthorSearch

s = AuthorSearch('AUTHLAST(Baimuratov) and AUTHFIRST(O)')
r = s.authors
id = r[0][0][7:]

au = AuthorRetrieval(id)

a = au.get_documents()
ind = 0


for i in range(len(a)):
    print('Site: Scopus')
    print('Title: ' + a[i][4])
    print('Authors: ' + a[i][13])
    print('Year: ' + a[i][17])
    print('Publisher: ' + a[i][18])
    print('Date: ' + a[i][16])
    print('Type: ' + a[i][6])
    print('Page: ' , a[i][26])
    print('                   ------------------------ ')

````
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/IMAGE%202022-04-04%2014:27:20.jpg)
