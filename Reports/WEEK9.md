# Arailym Abdrakhym
*    In the 9th week Arailym organized meetings with the members, and talked about the project and its progress,proof is below:
      + [Youtube](https://youtu.be/_UrIdmy4P54)

*   Also divided the tasks within the framework of the [Notion](https://www.notion.so/c96f404fd204448ca2ba0e2da8b3b767?v=3b7a048427274732b44eaa8537c5ba3e) program so that participants of group do not forget about the diplom work
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/9_notion.png)
    + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/9th-zadanya.front.png)
*          Parsing data from https://www.ebsco.com/ using Python:
   * learned scraping of [https://www.ebsco.com/](https://www.ebsco.com/products/research-databases)
       + ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/10_analyze%20web.png)
       + Coding part
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/ebsco.png)
    

# Albina Niyetullayeva
* Code site, Upload content, Upload design assets(Front-end)
  
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/1.jpeg)
 ````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="contact.css">
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
    <section class="container section-1">
<div class="rectangle">
  <br><br>
  <h1 class="reg" align="center">Contact</h1>
  <br><br>
  <div class="albi01">
    <div class="form-group">
      <input type="email" name="logemail" class="form-style" placeholder="Name" id="logemail" autocomplete="off">
    </div>  
    <div class="form-group mt-2">
      <input type="password" name="logpass" class="form-style" placeholder="Surname" id="logpass" autocomplete="off">
      <i class="input-icon uil uil-lock-alt"></i>

    </div>
    <div class="form-group mt-2">
      <input type="password" name="logpass" class="form-style" placeholder="E-mail" id="logpass" autocomplete="off">
      <i class="input-icon uil uil-lock-alt"></i>

    </div>
    <div class="form-group mt-2">
      <input type="password" name="logpass" class="form-style" placeholder="Quiestion" id="logpass" autocomplete="off">
      <i class="input-icon uil uil-lock-alt"></i>

    </div>
<a href="#" class="btn mt-4">submit</a>

</div>

  </div>
    <img src="contact2.png" align="right">
      
    </section>

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
.name2{
  margin-left: 50px;
  margin-top: 50px;
}
.name{
  font-family: Abhaya Libre ExtraBold;
font-size: 70px;
letter-spacing: 0em;
margin-left: 500px;
color: #686868;
left: 500px;
}
h2{
  padding-top: 50px;
  text-align: center;
  color: #686868;
}
.img{
  margin-top: 50px;
}

/* FOOTER */


.rectangle{
  
  color: red;
  position: absolute;
width: 600px;
height: 650px;
left: 40px;
top: 115px;

background: rgba(252, 90, 90, 0.17);
border: 1px solid #000000;
box-sizing: border-box;
box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
}

 .form-group{ 
  position: relative;
  display: block;
    margin: 10px 10px;
    padding: 0px;
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
  margin-left: 480px;
  margin-top: 20px;
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
  border: none;
  background-color: #ffeba7;
  color: #102770;
  box-shadow: 0 8px 24px 0 rgba(255,235,167,.2);
}
.btn:active,
.btn:focus{  
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
.btn:hover{  
  background-color: #102770;
  color: #ffeba7;
  box-shadow: 0 8px 24px 0 rgba(16,39,112,.2);
}
 ````
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/2.jpeg)
 ````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="about.css">
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
  <div>
<h1  class="name">Get to know us</h1>
<h2>We love helping you create a profile,
view and save posts</h2>
<h2>Our goal is to offer the best quality platform 
for working with publications</h2>
<div class="img">
	<img src="about.jpg" width="450px" height="350px">
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

.name{
  font-family: Abhaya Libre ExtraBold;
font-size: 70px;
letter-spacing: 0em;
text-align: center;
color: #686868;
}
h2{
  padding-top: 50px;
  text-align: center;
  color: #686868;
}
.img{
  margin-left: 570px;
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
 ````
   * ![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/3.jpeg)
  ````html
<!DOCTYPE html>
<html>
<head>
  <title></title>
  <meta charset="utf-8">
  <link rel="stylesheet" type="text/css" href="help.css">
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
  <div>


<div class="img">
	<div class="name2">
	<h1 >How do I register on in the site</h1>
</div>
	<img src="faq2.png" width="650px" height="550px">

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

.name{
  font-family: Abhaya Libre ExtraBold;
font-size: 70px;
letter-spacing: 0em;
text-align: center;
color: #686868;
}
h2{
  padding-top: 50px;
  text-align: center;
  color: #686868;
}
.img{
  margin-left: 770px;
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
 ````
 
# Aruzhan Kutzhan
* Data analize & research ScienceDirect
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/Aru_9.png)
* Here is an analysis of 5 sites.
Conclusion: to take from this analysis the most necessary for our site, to make it as convenient as possible for our users

# Shynar Toktar
* According to the plan, our task is Parsing data from Web of Science. I was analyzing the Website Web of Science. and I wrote a request. Result: the server understood the request, but refuses to authorize it.
* We decided not to waste time and chose another platform that has exactly the same level of importance. DOAJ is a platform of scientific articles in English.
* I created a DOAJ method that sends a request to the platform and receives data about the author and publications.


    + Coding part
````py
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

````
* Result:
![](https://github.com/SuleymanDemirelKazakhstan/diploma-project-april/blob/main/Diploma%20Document/figures/sh_9.png)
