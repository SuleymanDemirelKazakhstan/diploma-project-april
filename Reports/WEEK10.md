# Arailym Abdrakhym
*   In the 10th week Arailym organized meetings with the members & mentor 3 times a week, and talked about the project and its progress,proof is below:
      + [Youtube](https://www.youtube.com/watch?v=4l7rbaR2weo)

*   Also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants of group do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/10_1.1png.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/10_notion.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Снимок%20экрана%202022-03-28%20в%2015.26.06.png)
*          Parsing data from PubMed using Python:
   * learned scraping of [PubMed](https://pubmed.ncbi.nlm.nih.gov/)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/10_analyze.png)
       + Coding part
````py
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
````
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/583f53ea-efd7-4f36-a5c3-6ef00c81d741.jpg)  

# Albina Niyetullayeva
* Design confirmation from the team and upgrade all files.  improving existing design (Figma)
  
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/4.jpeg)
````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="home.css">

</head>
<body>
<header>
    <div class="company-logo"><img class="log" src="logo.jpg"></div>
    <nav class="navbar">
      <ul class="nav-items">
        <ol class="nav-item"><a href="#" class="nav-link1">About us</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link2">Help</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link3">Create account</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link4">Sing in</a></ol>
      </ul>
    </nav>

  </header>


<div class="4">
	<h1 class="search">Search Form</h1>
	<div class="rectangle1">
    <div class="form-group1">
      <h3>Name   <input type="email" name="logemail" class="form-style1" id="logemail" autocomplete="off"></h3>
    </div> <a href="#" class="btn mt-4">submit</a> </div>
    
    <div class="rectangle2">
    <div class="form-group2">
      <h3>   Surname   <input type="email" name="logemail" class="form-style2" id="logemail" autocomplete="off"></h3>
    </div><a href="#" class="btn mt-4">submit</a>  </div>
<div class="rectangle3">
	<div class="form-group3">
      <h3 class="orcid3">  ORCID  <input type="email" name="logemail" class="form-style3" id="logemail" autocomplete="off"></h3>
    </div><a href="#" class="btn mt-4">submit</a></div>
<div class="rectangle4">
	<div class="form-group4">
      <h3 class="sri4">  ScienceDirectoryID
  <input type="email" name="logemail" class="form-style4" id="logemail" autocomplete="off">    </div><a href="#" class="btn mt-4">submit</a></h3></div>
  <div class="rectangle5">
	<div class="form-group5">
      <h3 class="5">  ScopusID
  <input type="email" name="logemail" class="form-style5" id="logemail" autocomplete="off">    </div></h3></div>
  
</div>

</body>
</html>
````
````css


*,
*::before,
*::after {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}



body{
  
  background-image: url("back3.jpg");
              
}
/* ================= LOGO ================ */
.logo img {
  height: 25px;
  width: auto;
  display: block;
}

.log{
  border-top-left-radius: 50% 50%; 
  border-top-right-radius: 50% 50%; 
  border-bottom-right-radius: 50% 50%; 
  border-bottom-left-radius: 50% 50%;
}

/* ================= VARIABLE ================ */
:root {
  --primary-color: hsl(9, 94%, 61%);
  --primary-color-alt: hsl(28, 72%, 83%);
  --second-color: #3e537c;
  --second-color-alt: hsla(220, 33%, 36%, 65%);
  --third-color: hsl(220, 36%, 28%);
  --white-color: #fbfbfb;
  --white-color-alt: hsl(12, 14%, 93%);
  --dark-color: hsl(300, 100%, 0%);
}


/* ================= HEADER ================ */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: rgb(93, 24, 55);
  padding: 1rem 5rem;
}
.company-logo {
  font-size: 1rem;
  background: -webkit-linear-gradient(
    120deg,
  );
}
.nav-items {
  display: flex;
}
.nav-item {
  margin: 0 5rem;
}
/* ================= HOME ================ */
.nav-link1 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 420px;
}
.nav-link1::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link1:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
/* ================= ABOUT US ================ */
.nav-link2 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 560px;
}
.nav-link2::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link2:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
/* ================= Create acc ================ */
.nav-link3 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 250px;
}
.nav-link3::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link3:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
/* ================= Sing In ================ */
.nav-link4 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 120px;
}
.nav-link4::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link4:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}

/* DIV*/
.search{
  text-align: center;
}

/* FOOTER */

  .top-footer {
    flex-direction: row;
    justify-content: space-around;
    padding-top: 0rem;
  }
  .footer-title {
    font-size: 1rem;
    padding: 1rem 0;
  }
  .footer-items h3 {
    font-size: 0.9rem;
  }

  .end-footer {
    display: flex;
    flex-direction:  row;
    align-items: center;
    justify-content: center;
    background-color: #5D1837;
  }

.top-footer {
  background-color: rgb(93, 24, 65);
  display: flex;
  flex-direction: row;
}
.footer-title {
  font-weight: 500;
  font-size: 1.2rem;
  padding: 1rem 0;
  background-image: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.footer-items h3 {
  cursor: pointer;
  font-weight: 300;
  font-size: 1.1rem;
  padding: 0.1rem 0;
  color: var(--white-color-alt);
}
.footer-items h3:hover {
  text-decoration: underline;
}
.footer-items h3:last-child {
  padding-bottom: 2rem;
}

.end-footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #4D0525;
}
.copyright {
  color: var(--white-color-alt);
  padding: 1rem 0;
  font-size: 0.9rem;
}
.copyright b {
  font-weight: inherit;
  font-size: 0.9rem;
}
.designer {
  color: #3E1527;
  padding-bottom: 0.5rem;
  font-size: 0.9rem;
}
.designer:hover {
  text-decoration: underline;
}















.rectangle1{
  
  color: red;
  position: absolute;
width: 1100px;
height: 90px;
left: 200px;

top: 200px;

background: rgba(252, 90, 90, 0.17);
border: 1px solid #000000;
box-sizing: border-box;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.rectangle2{
  
  color: red;
  position: absolute;
width: 1100px;
height: 90px;
left: 200px;

top: 320px;

background: rgba(252, 90, 90, 0.17);
border: 1px solid #000000;
box-sizing: border-box;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.rectangle3{
  
  color: red;
  position: absolute;
width: 1100px;
height: 90px;
left: 200px;

top: 440px;

background: rgba(252, 90, 90, 0.17);
border: 1px solid #000000;
box-sizing: border-box;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

.rectangle4{
  
  color: red;
  position: absolute;
width: 1100px;
height: 90px;
left: 200px;

top: 560px;

background: rgba(252, 90, 90, 0.17);
border: 1px solid #000000;
box-sizing: border-box;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}








.form-group1  {
  color: red;
  top: 6px;
  left: 80px;
}
.form-group1{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
}
.form-style1 {
  padding: 13px 20px;
  padding-left: 55px;
  height: 33px;
  width: 35%;
  
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style1:focus,
.form-style1:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}







.form-group2  {
  color: red;
  top: -114px;
  left: 530px;
}
.form-group2{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
}
.form-style2 {
  padding: 13px 20px;
  padding-left: 55px;
  height: 33px;
  width: 35%;
  
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style2:focus,
.form-style2:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}


/* ORCID*/

.form-group3  {
  color: red;
  top: -114px;
  left: 310px;
}
.form-group3{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
}
.form-style3 {
  padding: 13px 20px;
  padding-left: 55px;
  height: 33px;
  width: 35%;
  
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style3:focus,
.form-style3:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}






.form-group4  {
  color: red;
  top: -114px;
  left: 220px;
}
.form-group4{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
}
.form-style4 {
  padding: 13px 20px;
  padding-left: 55px;
  height: 33px;
  width: 35%;
  
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style4:focus,
.form-style4:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}






.form-group5  {
  color: red;
  top: 410px;
  left: 500px;
}
.form-group5{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
}
.form-style5 {
  padding: 13px 20px;
  padding-left: 55px;
  height: 33px;
  width: 25%;
  
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style5:focus,
.form-style5:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}




.btn{  
  margin-left: 640px;
  margin-top: 10px;
  border-radius: 5px;
  height: 20px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
````

   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/5.jpeg)
````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="register.css">
  <script type="register.js"></script>
</head>
<body>
<header>
    <div class="company-logo"><img class="log" src="logo.jpg"></div>
    <nav class="navbar">
      <ul class="nav-items">
        <ol class="nav-item"><a href="#" class="nav-link1">About us</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link2">Help</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link3">Create account</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link4">Sing in</a></ol>
      </ul>
    </nav>

  </header>

 
    <!-- HOME SECTION -->
 <div class="section-1"></div> 
  <div class="center">

  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
                  <input class="checkbox" type="checkbox" id="reg-log" name="reg-log"/>
                  <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Sing In</h4>
                      <div class="form-group">
                        <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                        <i class="input-icon uil uil-at"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" class="btn mt-4">submit</a>
                                    <p class="mb-0 mt-4 text-center"><a href="#0" class="link">Forgot your password?</a></p>
                        </div>
                      </div>
                    </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Register</h4>
                      
                      <div class="form-group">
                        <input type="text" name="logname" class="form-style" placeholder="Your Full Name" id="logname" autocomplete="off">
                        <i class="input-icon uil uil-user"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                        <i class="input-icon uil uil-at"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" class="btn mt-4">submit</a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
  </div>
  </div>

   
    
    

  <footer>
    <div class="container top-footer">
      <!-- footer item 1 -->
      <div class="footer-item">
        <h2 class="footer-title">INSTAGRAM</h2>
        <div class="footer-items">
       
          
        </div>
      </div>
      <!-- footer item 2 -->
      <div class="footer-item">
        <h2 class="footer-title">TELEGRAM</h2>
        <div class="footer-items">
     
          
        </div>
      </div>
      <!-- footer item 3 -->
      <div class="footer-item">
        <h2 class="footer-title">G-MAIL</h2>
        <div class="footer-items">
   
          
        </div>
      </div>
      <!-- footer item 4 -->
      <div class="footer-item">
        <h2 class="footer-title">YOUTUBE</h2>
        <div class="footer-items">
 
          
        </div>
      </div>
    </div>
    <div class="container end-footer">
      <div class="copyright"> © 2022 - Team April </div>
    </div>
  </footer>
</body>
</html>
````
````css
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100;200;300;400");

*,
*::before,
*::after {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}


.center{
  margin-left: 400px;

}

body{
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  line-height: 1.7;
  background-image: url("back3.jpg");
  color: 0, 0%, 98%, 0.541;
                font-size: 30px;
                 height: 50px;
                 
}
a {

  cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
  text-decoration: none;
}
.link {

  color: #c4c3ca;
}
.link:hover {
  color: #ffeba7;
}
p {
  margin-left: 140px ;
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  margin-left: 160px ;
padding-bottom: 30px;

  font-weight: 600;
}

.section{
  position: relative;
  width: 100%;
  display: block;
}
.full-height{
  min-height: 100vh;
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: absolute;
  left: -9999px;
}
.checkbox:checked + label,
.checkbox:not(:checked) + label{

  position: relative;
  display: block;
  text-align: center;
  width: 200px;
  height: 16px;
  border-radius: 10px;
  top: 20px;
  padding-top: 20px;
  margin-left: 300px;
  cursor: pointer;
  background-color: #ffeba7;
}
.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before{
  
  position: absolute;  /* үстіндегі чек бокстын жүретін донгелек жері*/
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-image: url("https://img.icons8.com/flat-round/64/000000/circled-chevron-right.png");
  background-size: 38px;
  content: '\eb4f';
  z-index: 20;
  top: -10px;
  left: 1px;
  /* донгелектегы ректангл*/
  transition: all 0.5s ease;
}
.checkbox:checked + label:before {
  transform: translateX(165px) rotate(-270deg);
}


.card-3d-wrap {
  margin-left: 50px;
  position: relative;
  width: 700px;
  max-width: 100%;
  height: 400px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}
.card-3d-wrapper {
  width: 100%;   /* стындағы регистер ректангл*/
  height: 100%;   /* */
  position:absolute;    
  top: 0;
  left: 0;  
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out; 
}
.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #FED5D5;

  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}
.center-wrap{
  margin-left: 100px;
  margin-right: 10px;
  position: absolute;
  width: 70%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}


.form-group{ 
  position: relative;
  display: block;
    margin: 0;
    padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #ffeba7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.btn{  
  margin-left: 160px;
  margin-top: 30px;
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border-color: : green;
  background-color:   #FC5A5A;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}




.logo {
  position: absolute;
  top: 30px;
  right: 30px;
  display: block;
  z-index: 100;
  transition: all 250ms linear;
}
.logo img {
  height: 26px;
  width: auto;
  display: block;
}
/* ================= VARIABLE ================ */
:root {
  --primary-color: hsl(9, 94%, 61%);
  --primary-color-alt: hsl(28, 72%, 83%);
  --second-color: #3e537c;
  --second-color-alt: hsla(220, 33%, 36%, 65%);
  --third-color: hsl(220, 36%, 28%);
  --white-color: #fbfbfb;
  --white-color-alt: hsl(12, 14%, 93%);
  --dark-color: hsl(300, 100%, 0%);
}


/* ================= HEADER ================ */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: rgb(93, 24, 55);
  padding: 1rem 2rem;
}
.company-logo {
  font-size: 2.5rem;
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.nav-items {
  display: flex;
}
.nav-item {
  margin: 0 2rem;
}
.nav-link1 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 710px;
}
.nav-link1::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link1:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link2 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 750px;
}
.nav-link2::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link2:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link3 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 120px;
}
.nav-link3::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link3:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link4 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 80px;
}
.nav-link4::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link4:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.log{
  border-radius: 50%;
}

.log{
  border-top-left-radius: 50% 50%; 
  border-top-right-radius: 50% 50%; 
  border-bottom-right-radius: 50% 50%; 
  border-bottom-left-radius: 50% 50%;
}


.slogan .company-title {
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-top: 2rem;
  font-size: 1.5rem;
  font-weight: 600;
}
.slogan .company-slogan {
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-top: 1rem;
  font-size: 1.2rem;
  font-weight: 400;
  line-height: 1.8rem;
}



/* =============== FOOTER =============== */
.top-footer {
  background-color: rgb(93, 24, 65);
  display: flex;
  flex-direction: column;
}
.footer-title {
  font-weight: 500;
  font-size: 1.2rem;
  padding: 1rem 0;
  background-image: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.footer-items h3 {
  cursor: pointer;
  font-weight: 300;
  font-size: 1.1rem;
  padding: 0.1rem 0;
  color: var(--white-color-alt);
}
.footer-items h3:hover {
  text-decoration: underline;
}
.footer-items h3:last-child {
  padding-bottom: 2rem;
}

.end-footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--third-color);
}
.copyright {
  color: var(--white-color-alt);
  padding: 1rem 0;
  font-size: 0.9rem;
}
.copyright b {
  font-weight: inherit;
  font-size: 0.9rem;
}
.designer {
  color: hsla(0, 0%, 98%, 0.541);
  padding-bottom: 0.5rem;
  font-size: 0.9rem;
}
.designer:hover {
  text-decoration: underline;
}

/* =============== MEDIA QUERIES ======= */

@media screen and (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
  /* ================= HEADER ================ */
  header {
    padding: 0.5rem 1rem;
  }

}
@media (min-width: 769px) {
  header {
    padding: 1rem 5rem;
  }
  
  /* =============== FOOTER =============== */
  .top-footer {
    flex-direction: row;
    justify-content: space-around;
    padding-top: 0rem;
  }
  .footer-title {
    font-size: 1rem;
    padding: 1rem 0;
  }
  .footer-items h3 {
    font-size: 0.9rem;
  }

  .end-footer {
    display: flex;
    flex-direction:  row;
    align-items: center;
    justify-content: center;
    background-color: rgb(93, 24, 55)
  }
````
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/6.jpeg)
````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="register.css">
  <script type="register.js"></script>
</head>
<body>
<header>
    <div class="company-logo"><img class="log" src="logo.jpg"></div>
    <nav class="navbar">
      <ul class="nav-items">
        <ol class="nav-item"><a href="#" class="nav-link1">About us</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link2">Help</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link3">Create account</a></ol>
        <ol class="nav-item"><a href="#" class="nav-link4">Sing in</a></ol>
      </ul>
    </nav>

  </header>

 
    <!-- HOME SECTION -->
 <div class="section-1"></div> 
  <div class="center">

  <div class="section">
    <div class="container">
      <div class="row full-height justify-content-center">
        <div class="col-12 text-center align-self-center py-5">
          <div class="section pb-5 pt-5 pt-sm-2 text-center">
                  <input class="checkbox" type="checkbox" id="reg-log" name="reg-log"/>
                  <label for="reg-log"></label>
            <div class="card-3d-wrap mx-auto">
              <div class="card-3d-wrapper">
                <div class="card-front">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Sing In</h4>
                      <div class="form-group">
                        <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                        <i class="input-icon uil uil-at"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" class="btn mt-4">submit</a>
                                    <p class="mb-0 mt-4 text-center"><a href="#0" class="link">Forgot your password?</a></p>
                        </div>
                      </div>
                    </div>
                <div class="card-back">
                  <div class="center-wrap">
                    <div class="section text-center">
                      <h4 class="mb-4 pb-3">Register</h4>
                      
                      <div class="form-group">
                        <input type="text" name="logname" class="form-style" placeholder="Your Full Name" id="logname" autocomplete="off">
                        <i class="input-icon uil uil-user"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="email" name="logemail" class="form-style" placeholder="Your Email" id="logemail" autocomplete="off">
                        <i class="input-icon uil uil-at"></i>
                      </div>  
                      <div class="form-group mt-2">
                        <input type="password" name="logpass" class="form-style" placeholder="Your Password" id="logpass" autocomplete="off">
                        <i class="input-icon uil uil-lock-alt"></i>
                      </div>
                      <a href="#" class="btn mt-4">submit</a>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
      </div>
  </div>
  </div>

   
    
    

  <footer>
    <div class="container top-footer">
      <!-- footer item 1 -->
      <div class="footer-item">
        <h2 class="footer-title">INSTAGRAM</h2>
        <div class="footer-items">
       
          
        </div>
      </div>
      <!-- footer item 2 -->
      <div class="footer-item">
        <h2 class="footer-title">TELEGRAM</h2>
        <div class="footer-items">
     
          
        </div>
      </div>
      <!-- footer item 3 -->
      <div class="footer-item">
        <h2 class="footer-title">G-MAIL</h2>
        <div class="footer-items">
   
          
        </div>
      </div>
      <!-- footer item 4 -->
      <div class="footer-item">
        <h2 class="footer-title">YOUTUBE</h2>
        <div class="footer-items">
 
          
        </div>
      </div>
    </div>
    <div class="container end-footer">
      <div class="copyright"> © 2022 - Team April </div>
    </div>
  </footer>
</body>
</html>
````
````css
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@100;200;300;400");

*,
*::before,
*::after {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}


.center{
  margin-left: 400px;

}

body{
  font-family: 'Poppins', sans-serif;
  font-size: 15px;
  line-height: 1.7;
  background-image: url("back3.jpg");
  color: 0, 0%, 98%, 0.541;
                font-size: 30px;
                 height: 50px;
                 
}
a {

  cursor: pointer;
  transition: all 200ms linear;
}
a:hover {
  text-decoration: none;
}
.link {

  color: #c4c3ca;
}
.link:hover {
  color: #ffeba7;
}
p {
  margin-left: 140px ;
  font-weight: 500;
  font-size: 14px;
  line-height: 1.7;
}
h4 {
  margin-left: 160px ;
padding-bottom: 30px;

  font-weight: 600;
}

.section{
  position: relative;
  width: 100%;
  display: block;
}
.full-height{
  min-height: 100vh;
}
[type="checkbox"]:checked,
[type="checkbox"]:not(:checked){
  position: absolute;
  left: -9999px;
}
.checkbox:checked + label,
.checkbox:not(:checked) + label{

  position: relative;
  display: block;
  text-align: center;
  width: 200px;
  height: 16px;
  border-radius: 10px;
  top: 20px;
  padding-top: 20px;
  margin-left: 300px;
  cursor: pointer;
  background-color: #ffeba7;
}
.checkbox:checked + label:before,
.checkbox:not(:checked) + label:before{
  
  position: absolute;  /* үстіндегі чек бокстын жүретін донгелек жері*/
  display: block;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background-image: url("https://img.icons8.com/flat-round/64/000000/circled-chevron-right.png");
  background-size: 38px;
  content: '\eb4f';
  z-index: 20;
  top: -10px;
  left: 1px;
  /* донгелектегы ректангл*/
  transition: all 0.5s ease;
}
.checkbox:checked + label:before {
  transform: translateX(165px) rotate(-270deg);
}


.card-3d-wrap {
  margin-left: 50px;
  position: relative;
  width: 700px;
  max-width: 100%;
  height: 400px;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  perspective: 800px;
  margin-top: 60px;
}
.card-3d-wrapper {
  width: 100%;   /* стындағы регистер ректангл*/
  height: 100%;   /* */
  position:absolute;    
  top: 0;
  left: 0;  
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  transition: all 600ms ease-out; 
}
.card-front, .card-back {
  width: 100%;
  height: 100%;
  background-color: #FED5D5;

  position: absolute;
  border-radius: 6px;
  left: 0;
  top: 0;
  -webkit-transform-style: preserve-3d;
  transform-style: preserve-3d;
  -webkit-backface-visibility: hidden;
  -moz-backface-visibility: hidden;
  -o-backface-visibility: hidden;
  backface-visibility: hidden;
}
.card-back {
  transform: rotateY(180deg);
}
.checkbox:checked ~ .card-3d-wrap .card-3d-wrapper {
  transform: rotateY(180deg);
}
.center-wrap{
  margin-left: 100px;
  margin-right: 10px;
  position: absolute;
  width: 70%;
  padding: 0 35px;
  top: 50%;
  left: 0;
  transform: translate3d(0, -50%, 35px) perspective(100px);
  z-index: 20;
  display: block;
}


.form-group{ 
  position: relative;
  display: block;
    margin: 0;
    padding: 0;
}
.form-style {
  padding: 13px 20px;
  padding-left: 55px;
  height: 48px;
  width: 100%;
  font-weight: 500;
  border-radius: 4px;
  font-size: 14px;
  line-height: 22px;
  letter-spacing: 0.5px;
  outline: none;
  color: #c4c3ca;
  background-color:   #ffffff;
  border: none;
  -webkit-transition: all 200ms linear;
  transition: all 200ms linear;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.form-style:focus,
.form-style:active {
  border: none;
  outline: none;
  box-shadow: 0 4px 8px 0 rgba(21,21,21,.2);
}
.input-icon {
  position: absolute;
  top: 0;
  left: 18px;
  height: 48px;
  font-size: 24px;
  line-height: 48px;
  text-align: left;
  color: #ffeba7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.form-group input:-ms-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:-moz-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input::-webkit-input-placeholder  {
  color: #c4c3ca;
  opacity: 0.7;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-ms-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus:-moz-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}
.form-group input:focus::-webkit-input-placeholder  {
  opacity: 0;
  -webkit-transition: all 200ms linear;
    transition: all 200ms linear;
}

.btn{  
  margin-left: 160px;
  margin-top: 30px;
  border-radius: 4px;
  height: 44px;
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  -webkit-transition : all 200ms linear;
  transition: all 200ms linear;
  padding: 0 30px;
  letter-spacing: 1px;
  display: -webkit-inline-flex;
  display: -ms-inline-flexbox;
  display: inline-flex;
  -webkit-align-items: center;
  -moz-align-items: center;
  -ms-align-items: center;
  align-items: center;
  -webkit-justify-content: center;
  -moz-justify-content: center;
  -ms-justify-content: center;
  justify-content: center;
  -ms-flex-pack: center;
  text-align: center;
  border-color: : green;
  background-color:   #FC5A5A;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #5D1837;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}




.logo {
  position: absolute;
  top: 30px;
  right: 30px;
  display: block;
  z-index: 100;
  transition: all 250ms linear;
}
.logo img {
  height: 26px;
  width: auto;
  display: block;
}
/* ================= VARIABLE ================ */
:root {
  --primary-color: hsl(9, 94%, 61%);
  --primary-color-alt: hsl(28, 72%, 83%);
  --second-color: #3e537c;
  --second-color-alt: hsla(220, 33%, 36%, 65%);
  --third-color: hsl(220, 36%, 28%);
  --white-color: #fbfbfb;
  --white-color-alt: hsl(12, 14%, 93%);
  --dark-color: hsl(300, 100%, 0%);
}


/* ================= HEADER ================ */
header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: rgb(93, 24, 55);
  padding: 1rem 2rem;
}
.company-logo {
  font-size: 2.5rem;
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.nav-items {
  display: flex;
}
.nav-item {
  margin: 0 2rem;
}
.nav-link1 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 710px;
}
.nav-link1::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link1:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link2 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  right: 750px;
}
.nav-link2::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link2:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link3 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 120px;
}
.nav-link3::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link3:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.nav-link4 {
  font-size: 1.1rem;
  letter-spacing: 0.05rem;
  position: relative;
  background: -webkit-linear-gradient(
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  left: 80px;
}
.nav-link4::before {
  content: "";
  background: linear-gradient(var(--primary-color), var(--primary-color-alt));
  width: 100%;
  height: 0.05rem;
  position: absolute;
  left: 0;
  bottom: 0;
  transform: scaleX(0);
  transform-origin: bottom right;
  transition: transform 150ms;
}
.nav-link4:hover::before {
  transform: scaleX(1);
  transform-origin: bottom left;
}
.log{
  border-radius: 50%;
}

.log{
  border-top-left-radius: 50% 50%; 
  border-top-right-radius: 50% 50%; 
  border-bottom-right-radius: 50% 50%; 
  border-bottom-left-radius: 50% 50%;
}


.slogan .company-title {
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-top: 2rem;
  font-size: 1.5rem;
  font-weight: 600;
}
.slogan .company-slogan {
  background: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-top: 1rem;
  font-size: 1.2rem;
  font-weight: 400;
  line-height: 1.8rem;
}



/* =============== FOOTER =============== */
.top-footer {
  background-color: rgb(93, 24, 65);
  display: flex;
  flex-direction: column;
}
.footer-title {
  font-weight: 500;
  font-size: 1.2rem;
  padding: 1rem 0;
  background-image: -webkit-linear-gradient(
    120deg,
    var(--primary-color-alt),
    var(--primary-color)
  );
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
.footer-items h3 {
  cursor: pointer;
  font-weight: 300;
  font-size: 1.1rem;
  padding: 0.1rem 0;
  color: var(--white-color-alt);
}
.footer-items h3:hover {
  text-decoration: underline;
}
.footer-items h3:last-child {
  padding-bottom: 2rem;
}

.end-footer {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--third-color);
}
.copyright {
  color: var(--white-color-alt);
  padding: 1rem 0;
  font-size: 0.9rem;
}
.copyright b {
  font-weight: inherit;
  font-size: 0.9rem;
}
.designer {
  color: hsla(0, 0%, 98%, 0.541);
  padding-bottom: 0.5rem;
  font-size: 0.9rem;
}
.designer:hover {
  text-decoration: underline;
}

/* =============== MEDIA QUERIES ======= */

@media screen and (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
  /* ================= HEADER ================ */
  header {
    padding: 0.5rem 1rem;
  }

}
@media (min-width: 769px) {
  header {
    padding: 1rem 5rem;
  }
  
  /* =============== FOOTER =============== */
  .top-footer {
    flex-direction: row;
    justify-content: space-around;
    padding-top: 0rem;
  }
  .footer-title {
    font-size: 1rem;
    padding: 1rem 0;
  }
  .footer-items h3 {
    font-size: 0.9rem;
  }

  .end-footer {
    display: flex;
    flex-direction:  row;
    align-items: center;
    justify-content: center;
    background-color: rgb(93, 24, 55)
  }

````

# Aruzhan Kutzhan

* The sites with which I conducted an analysis, studied the filtering for publication on our site
We will filter the data more precisely, we will make a function where it will check whether the publication is repeated in the list, and will delete repeated publications. The first week was studying our function, the second week was already writing code.
Since our site will collect a number of publications, it is important to us that publications are not repeated. This is an important part of our work.
 Referring to this data, and to the mistakes that are usually made during filtering, we will create a function for our site.
   + [https://www.internet-technologies.ru/articles/php-filtraciya-dannyh.html](https://www.internet-technologies.ru/articles/php-filtraciya-dannyh.html)
   + [https://habr.com/ru/post/143035/](https://habr.com/ru/post/143035/)

# Shynar Toktar
*  This week I created a new method as the main one that runs parsing methods for 4 sites. to get results from all sites on the same types, I added lists and dictionaries to the methods and changed some points.
````py
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
````
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/90cfadb1-07c6-486e-beae-b5b99eefe2af.jpg)
