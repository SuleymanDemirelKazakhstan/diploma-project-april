# Arailym Abdrakhym
*    In the 12th week Arailym organized meetings with the members and mentor, and talked about the project and its progress,proof is below:
      + [Youtube]()

*   Also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants of group do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/12.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/12_1.png)

   * Coding part of Matplotlib
 ````py
 from cProfile import label
from collections import Counter
from turtle import color
from matplotlib import pyplot as plt
import  numpy as np

datainput=[{'year' : 2022},{'year' : 2022},{'year' : 2028},{'year' : 2028},{'year' : 2029},{'year' : 2023},{'year' : 2021},{'year' : 2020},{'year' : 2021}, {'year' : 2018},{'year' : 2019},{'year' : 2021},{'year' : 2020},{'year' : 2022}]


llist=[]
cnt = Counter()
for dates in datainput:
    year = dates['year']
    cnt[year] += 1

yearses=[]
popu=[]
for item in cnt.most_common(15):
    yearses.append(item[0])
    popu.append(item[1])

#plt.plot(yearses, popu,color= '#444444', linewidth=3, label='degree')
plt.bar(yearses, popu,color= '#5a7d9a', linewidth=3, label='degree')



plt.title("KPI of publication work's")
plt.xlabel("Years")
plt.ylabel("Number of publication")
plt.tight_layout()
plt.legend()
plt.grid() 


plt.show()
#plt.savefig('plot.png')
 ````
   ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/matplotlibres.jpg)
      

# Albina Niyetullayeva
* Learned Formspree
  
   * is a form backend, API, and email service for HTML & JavaScript forms. It's the simplest way to embed custom contact us forms, order forms.
# Aruzhan Kutzhan

* Going to filter and displays the final result on the website


# Shynar Toktar
*      Latex template for pdf file
  
   + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Sh_1.jpg)
   + Latex template code
````latex
\documentclass[12pt]{article}

%% Define some new colors
\usepackage{xcolor}
\definecolor{mBlue}{RGB}{51, 77, 167}
\newcommand{\blue}[1]{{\color{mBlue}#1}}

%% Page and text formatting
\usepackage[left=1.0in, right=1.0in, top=1.0in, bottom=1.0in]{geometry} % margins
\usepackage{setspace}
\singlespacing % No more than 6 lines of text per inch
\usepackage[T1]{fontenc}
\usepackage{times}

%% Set up footer
\usepackage{fancyhdr}
\fancypagestyle{CVfooter}
{
 \lhead{}
 \chead{}
 \rhead{}
 \lfoot{}
 \cfoot{}
 \rfoot{\small{\thepage/9}}
 \renewcommand{\headrulewidth}{0.0pt}
 \renewcommand{\footrulewidth}{0.5pt}
}

%% Set up hyperlinks
\usepackage[linktoc=page]{hyperref}
\hypersetup{
  colorlinks = true,
  urlcolor = mBlue,
  citecolor = mBlue,
  linkcolor = mBlue,
}


%% Reduce whitespace around lists (globally)
\ifx\pdfoutput\undefined
\usepackage{graphicx}
\else
\usepackage[pdftex]{graphicx}
\fi
\usepackage{enumitem}
\usepackage{graphicx}%������� �������� ����������
\usepackage{float}%"���������" ��������

\usepackage{wrapfig}%��������� ����� (������, �������� � �������)
\setlist[itemize]{nosep,left=0pt}
\setlist[enumerate]{nosep}
\setlist[description]{nosep}

%% Formatting for sections
\usepackage[compact]{titlesec}
\titleformat*{\section}{\normalsize\bfseries}
\titlespacing*{\section}{0mm}{2mm}{1mm}[0mm] % left top bottom right

\usepackage[export]{adjustbox}

\begin{document}
\pagestyle{CVfooter}

\begin{minipage}{.2\linewidth}
\centering
\includegraphics[width = 2.25cm, height=3cm,frame, left]{Profile.jpg}
\vspace{2mm}
\end{minipage}
\begin{minipage}{.7\linewidth}
\noindent\begin{tabular}{l*{3}{l}r}
Name: & \VAR{NAME}\\[0.3cm]
Email: & \href{\VAR{EMAIL}}{\VAR{EMAIL}} \\ [0.3cm]
Position: & \VAR{POS}\\ [0.3cm]
Affilation: & \VAR{AFF} \\ [0.3cm]
\end{tabular}
\end {minipage}

\hline

\section*{Publications}
\vspace{2mm}

\begin{enumerate}

    \VAR{PUBLIST}

\end{enumerate}

\end{document}
````
   + Code for inserting data about the publication and about the author on the template

````py

import subprocess
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

    '''
    if os.path.isfile('restex.tex'):
        print('The file is present.')
    else:
        print('The file is not present.')


    process = subprocess.Popen([
        'latex',  # Or maybe 'C:\\Program Files\\MikTex\\miktex\\bin\\latex.exe
        '-output-format=pdf',
        '-job-name=' + 'res_pdf.pdf',
        r'C:/Users/User/Desktop/Diploma Project/restex.tex'])
    process.wait()
    '''

run()
````
+ Result
+ ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Sh_2.jpg)
