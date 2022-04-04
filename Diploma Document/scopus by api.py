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
