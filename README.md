# CSS 410 Research tools and methods
## Team members
+ Abdrakhym Arailym(180103070)-Project manager, Python developer(GitHub account: https://github.com/Arailym-Abdrakhym)
+ Toktar Shynar(180103079)- Backend Developer (GitHub account: https://github.com/ToktarShynar180103079)
+ Kutzhan Aruzhan(180103137)- Data-Analyst, Data Engineer(GitHub account: https://github.com/Aruzhan180103137)
+ Niyetullayeva Albina(180103018)- Designer UX/UI,Frontend Developer (GitHub account: https://github.com/Niyetullayeva)




## Project 
Our project will make possible to view and download the list of researcher's publications, and researchers can create their own portfolio, in which a list of publications will automatically appear and researchers add additional information if desired.

## Alternative / Market research 
Alternative sites - Scopus, IEEEXplore, Google Scholar, Science Direct, Web of science.
These sites are databases that houses articles from many different publishers. Each of them does not give a complete list of the publications of the researchers our task is to combine, filter and as a result collect a complete list of the works of the researchers.

[Scopus](https://www.scopus.com/home.uri?zone=header&origin=) is a website containing publications and citations. Scopus contains profiles of authors, the number of publications and their bibliographic data, references and detailed information about the number of citations received
by each published document.


__Advantages__
1. There is an advanced search by publications, by author and by organizations
2. Search parameters
3. There are graphics on the areas of the author’s publication

__Disadvantages__
1. Access to data only if the user logs in from an organization allowed by Scopus


[IEEE Xplore](https://ieeexplore.ieee.org/Xplore/home.jsp) is a research platform that provides access to articles, publications, and conference materials. The database mainly includes materials from the Institute of Electrical and Electronics Engineers) and the Institute of Engineering and Technology.

__Advantages__
1. Advanced search on the site
2. It is possible to adjust the year during the search, which is convenient for the user
3. It is possible to filter by publication names
4. It is possible to export by these parameters

__Disadvantages__
1. There is no access to the publication itself, but there is an opportunity to buy the publication

[Google Scholar](https://scholar.google.com/) is a free, accessible search engine for full texts of scientific publications of all formats and disciplines. 

__Advantages__
1. When searching, it is possible to configure the year, time, etc.
2. There is the author’s data in the form of graphics
3. It is possible to download the publication for free


[Science Direct](https://www.sciencedirect.com/) is a database of scientific research. It belongs to the publisher Elsevier and contains about 10 million articles. The articles are grouped into four main sections: physical and engineering sciences, natural sciences, medical sciences, as well as social and humanitarian sciences.

__Advantages__
1. Every can view the publication for free and download all publications
2. Advanced Search

__Disadvantages__
1. No author profile

[Web of Science](https://access.clarivate.com/login?app=wos&alternative=true&shibShireURL=https:%2F%2Fwww.webofknowledge.com%2F%3Fauth%3DShibboleth&shibReturnURL=https:%2F%2Fwww.webofknowledge.com%2F&roaming=true) is a platform from Clarivate Analytics. It consists of an extensive collection of bibliographic databases, citations, and links to scientific publications. 

__Advantages__
1. Advanced Search
2. Exporting data by these parameters

__Disadvantages__
1. Limited access, only login for certain organizations.

## Goals
Developing web application/ web scraping system for automatisation process of bibliometric data collection. 
Create a web page that will create a portfolio of publications from different sources. The website will collect a list of references and bibliometric information.

## User personas 
SDU  STAFF & Researchers  

## User stories
1. As a teacher, I want to see my work statistics on your website
2. As a user, I want all your profiles to have a standard template.
3. As a student, I want to see the achievements of our teachers in order to motivate myself


## Sitemap. Page descriptions 

+ Sitemap:


![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/52a9f476-6221-41a5-a90d-dce00f768a9e.jpg)





+ Page descriptions: 


|                Page                    |                  Elements                                                                                        |
|----------------------------------------|------------------------------------------------------------------------------------------------------------------|
|Home                                    |Logo <br> Help: FAQ / Contact us <br> Sign in/up <br> Search form: surname and name and orcid and ID <br> About us|
|About us                                |About our product                                                                                                 |
|Sign in/up                              |Data about users                                                                                                  |
|Results                                 |Result table <br> Statistics <br> Create portfolio <br> Export to csv                                             |
|Portfolio                               |Edit button <br> Import photo <br> List of publications <br> Send to github/ export to pdf                        |
|Account                                 |Information about user <br> Last edit/create portfolio                                                            |
|Help                                    |Contact us <br> FAQ                                                                                               |


## Describe technologies that will be used, describe domain (classes, ERD) 
+ LANGUAGES:HTML, CSS, and JavaScript,  Python, php, Oracle, R 
+ LIBRARIES: Serpapi, urllib, pandas, sqlite3
+ FRAMEWORKS:Django
+ API:  scopus api
+ Tools: Figma, Latex, etc.

+ ER-diagram:

![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/24d97ce3-8cf6-4e47-8d82-69182521fc67.jpg)


## Mockups, Wireframes

![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.34.23.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.34.48.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.34.58.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.35.15.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.35.27.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.35.40.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.35.47.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.35.59.png)
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-02-13%20в%2016.36.07.png)


## Non-functional requirements
The website will automatically collect a list of references and all bibliometric information about publications from various sources: such as Scopus, Scolap, IEEEXplore, Science direct. 
And after preparing the portfolio, we should be able to export the document as CSV or PDF. And also during the export, there should be a single standard template in the document.
The WEBSITE should work in all modern browsers, work well and look good on all screen sizes.


## Risks 
+ The protective actions of sites can complicate the parsing process.
+ Due to the large number of requests, access to the site may be blocked or restricted, which will not allow collecting all the information.
+ Parsers are configured for a specific page design, and websites periodically update their content, in which case parsing may not work on the updated page.
+ Our project is being done during a pandemic and there is a risk that a participant from our team may get sick, at this time we will need to replace him or finish his work.



## Future iterations
If the SDU accepts our project (website), then there will be a link to our website on the official website.
In the future, we want to make a system for collecting user projects and also add a number of copyrights to the user.
We want users of other universities to also be able to use our product (website).


