# WebPageScrapers
  A Python3 script that scrapes all the href links from a webpage

# Dependency modules:
  1. Beautifulsoup4
  2. requests

# Usage with examples:
Example1: Scraping https webpage: 
  "python scrapeAllHyperlinksFromWebpage.py https://www.yahoo.co.in"
  
  Scraping following webpage: https://www.yahoo.co.in
  link: https://login.yahoo.com?.src=search&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.search.yahoo.com%2F%3Ffr2%3Dinr&pspid=2114723002&activity=header-signin
  link: https://in.search.yahoo.com/search?ei=UTF-8&fr2=p%3As%2Cv%3Asfp%2Cm%3Afeaturebar&p=coronavirus
  link: https://login.yahoo.com?.src=search&.intl=in&.lang=en-IN&.done=
  link: https://in.mail.yahoo.com/?.intl=in&.lang=en-IN
  link: https://help.yahoo.com/kb/index?page=content&y=PROD_ACCT&locale=en_IN&id=SLN35842
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=COVID-19+in+India&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Anil+Deshmukh&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Ajit+Doval&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Ahmednagar+fire&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Yogi+Adityanath&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Digital+Marketing+Strategy&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Akhilesh+Yadav&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=KL+Rahul&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=Aryan+Khan&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://in.search.yahoo.com/search?ei=UTF-8&p=ICC+Men%27s+T20+World+Cup&fr=sfp-tts&fr2=p%3Asfp%2Cm%3Atn%2Cct%3Aall%2Ckt%3Aorg
  link: https://help.yahoo.com/l/in/yahoo/helpcentral/
  link: https://legal.yahoo.com/in/en/yahoo/privacy/products/searchservices/index.html
  link: https://legal.yahoo.com/in/en/yahoo/terms/otos/index.html
  link: http://advertisingcentral.yahoosearchmarketingin.com/
  Total links scraped from https://www.yahoo.co.in are: 19

Example2: Scraping http webpage: 
  "python scrapeAllHyperlinksFromWebpage.py http://www.webscantest.com/"
  
  Scraping following webpage: http://www.webscantest.com/
  link: /login.php
  link: https://www.rapid7.com/products/appspider/
  link: jsmenu/auto_datastore.php
  link: jsmenu/auto_shutterdb.php
  link: jsmenu/auto_crosstraining.php
  link: csrf
  link: cors/cors.php
  link: soap/demo/
  link: rest/demo/
  link: react/index/
  link: angular/
  link: jsmenu/auto_osrun.php
  link: jsmenu/cookie_set_coffeepits.php
  link: jsmenu/dynalink_myfiles.php
  link: jsmenu/dynalink_rfplaces.php
  link: jsmenu/gotoframeme.php?foo%3D0+bar%3D+url%3Dhttps%3A%2F%2Fauth.ntobjectives.com+dr%3Dsomedir
  link: jsmenu/gotoajax.php
  link: gonowhere
  link: static/
  link: xmldb/index.php
  link: infodb/index.php
  link: business
  link: images/bouncingmike.jpg?a=b
  link: /privacy.php
  Total links scraped from http://www.webscantest.com/ are: 24
