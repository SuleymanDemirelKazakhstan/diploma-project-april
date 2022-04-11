import os
from parsing_all import *

AuthorInf = {'Name' : 'Bogdanchikov Andrey', 'Email' : 'andrey.bogdanchikov@sdu.edu.kz', 'Position':'Associate Professor in Computer Sciences Department', 'Affilation':'Suleyman Demirel University'}

def getbibtext(pub_list):
    ResText = ''
    for item in pub_list:
        ResText = ResText + '\n\item ' + item['Authors'] + ', ' \
                  + '\href{' + item['Link'] + '}{' + item['Title'] + '}, '\
                  + item['Where published'] + ', ' \
                  + item['Year'] + ', pp.' \
                 # + item['PP.'] + '.'
    return ResText
def run():
    PubList = parsing('Bogdanchikov', 'Andrey')
    ResText = getbibtext(PubList)
    #open tex template
    with open('sometexfile.tex') as template_file:
        global latex_code
        latex_code = template_file.read()
        print(latex_code)
    # write and save tex file
    tex_filename = 'restex.tex'
    with open(tex_filename, 'w') as latex_file:
        latex_code = latex_code.replace(r'\VAR{NAME}', AuthorInf['Name'])
        latex_code = latex_code.replace(r'\VAR{EMAIL}', AuthorInf['Email'])
        latex_code = latex_code.replace(r'\VAR{POS}', AuthorInf['Position'])
        latex_code = latex_code.replace(r'\VAR{AFF}', AuthorInf['Affilation'])
        latex_code = latex_code.replace(r'\VAR{PUBLIST}', ResText)
        latex_file.write(latex_code)
    print(latex_code)
    print(f'Generated {tex_filename}')

    os.system("pdflatex restex.tex")
run()