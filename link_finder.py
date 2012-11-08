#/usr/local/bin/python
###Sorts through all the websites for terms

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import cgitb
import os
cgitb.enable()


all_sites = []#list will store all URLs for news sites
siteTerms = {} #save a dictionary with id for the website and value is another dictionary with the terms

#asks user for new web address
def addurl():
##    website = input('http://')
##    siteName= input('Please uniquely identify the site (i.e. "nytimes"): ')
    website = 'http://' + 'www.nytimes.com'
    siteName = 'm'
    all_sites.append(website)
    return [website,siteName]

def getLinks(url):
    soup = BeautifulSoup(urlopen(url).read())
    aTags=[]
    aTags = soup.find_all('a')
    links=[]
    for link in aTags:
        href = link.get('href')
        if re.search(r'(.com|.org|.edu|.net)',href):
            pass
        elif re.search(r'(mailto:)',href):
            pointer = None
        else:
            href = url +"/"+ href
        if href != None: links.append(href)
    print(links)
    return links

goodURLs= []
def searchLinks(url):
    soup = BeautifulSoup(urlopen(url).read())
    uses = []
    try:
        title= soup.title
        if re.search(r'.*(romney|Romney|obama|Obama|Presidential Debate).*', str(title)):
            goodURLs.append(url)
        else: print('no uses at',url)
        print(goodURLs)
    except:
        print('no uses at',url)
    
    

def main():
    url = addurl()
    links = getLinks(url[0])
    for url in links:
        searchLinks(url)

main()
