#!/usr/bin/env python3
import sys
import requests
from bs4 import BeautifulSoup

url = sys.argv[1]
print ("Scraping following webpage: %s" % url)
try:
    response = requests.get(url)
except:
    print ("Oops! That does not look like a valid url or cannot be scraped. Try with a new one")
    sys.exit()
soup = BeautifulSoup(response.text, 'html.parser')
total_links = 0
for a in soup.find_all('a', href=True):
    if a.text:
        print ("link: %s" % a['href'])
        total_links = total_links+1
print ('Total links scraped from %s are: %d' % (url, total_links))
