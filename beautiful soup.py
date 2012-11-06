#!/usr/local/bin/python
###Sorts through all the websites for terms


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import cgitb
cgitb.enable()


all_sites = []#list will store all URLs for news sites
siteTerms = {} #save a dictionary with id for the website and value is another dictionary with the terms

#asks user for new web address
def addurl():
    print("""
    WEBSITE WORD COUNTER
    -Supply a website, and a name
    -Get a JSON file with word counts saved under that name
    -use get('website name','someWord') to retrieve a count of uses of someWord on the website.
    """)
    website = input('http://')
    siteName= input('Please uniquely identify the site (i.e. "nytimes"): ')
    website = 'http://' + website
    all_sites.append(website)
    return [website,siteName]

def getHomePageText(URL):
    soup = BeautifulSoup(urlopen(URL).read())
    siteText = soup.body.get_text()
    #print(siteText)
    return siteText

def saveTerms(string): #returns a list of words
    wordList = []
    wordList = re.findall(r'(romney|Romney|obama|Obama)+', string) #takes just the words
    return wordList

#produces a dictionary of terms and their number of uses
def countTerms(someList):
    terms = {}
    for word in someList:
        word = str(word).lower() #keeps all the words lowercase
        if word not in terms:
            terms[word] = 1
        else:
            terms[word] += 1
    sortedTerms = sorted(terms)
##    print("\n'term': count")
    for i in sortedTerms:
        print(i+": "+str(terms[i]))
    return terms

#
def formatJSON(someSite,someDict):
    jsonObj = {someSite:someDict}
    jsonFile = open('../json files/'+someSite+'.json','w')
    json.dump(jsonObj,jsonFile)
    jsonFile.close()
    return jsonObj

def get(name, term):
    return siteTerms[name][term]

def main():
##    counter = getCounter()
    URL = addurl()
    print(URL);
    siteID= URL[1]
    siteTerms[siteID] = countTerms(saveTerms(getHomePageText(URL[0])))
    formatJSON(siteID,siteTerms[siteID])
    #print(siteTerms[siteID])



if __name__ == "__main__": main()

