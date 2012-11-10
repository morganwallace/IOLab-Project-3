#Exports JSON with Obama Sentences and Romney Sentences

import json
import os

article = input("paste the language of the article here: ")
article =  article.encode('utf-8')
article.replace(r'\u2014','')
article =  article.encode('ascii')
pubNo = input('what is the puclication number? ')
source = input("Newspaper: ")
debateNo = input("Debate number: ")
URL = input("url: ")

obamaSentences= []
romneySentences= []


#find sentences with obama or romney in it
def findInSentences(articleText):
    obamaSaid = ''
    romneySaid = ''
    allSentences=articleText.split('.')
    for i in article.split('.'):
        if 'Romney' in i:
            i.replace('-','')
            i.replace('\\n','')#remove whitespace
            i.replace('\\t','')#remove whitespace            
            i.replace('\\','')
            romneySentences.append(i)
        if 'Obama' in i:
            i.replace('-','')
            i.replace('\\n','')#remove whitespace
            i.replace('\\t','')#remove whitespace            
            i.replace('\\','')
            obamaSentences.append(i)
    for sentence in romneySentences: romneySaid+=". " + sentence
    romneySaid = romneySaid[1:]
    for sentence in obamaSentences: obamaSaid+=". " + sentence
    obamaSaid = obamaSaid[1:]
    return romneySaid, obamaSaid
    
#Export for sentiment analysis
def saveJSON(url,pubName,obamaSentences,romneySentences,publicationNo,debateNo):
    jsFile = open('data.js','a')
    jsFile.write(('var p'+publicationNo+'d'+debateNo+' = {"source": '+pubName+', "Osentences": '+obamaSentences+', "Rsentences": '+romneySentences+'}\n\n').encode('ascii'))
    jsFile.close()


def main():
    romneySaid = findInSentences(article)[0]
    obamaSaid = findInSentences(article)[1]
    saveJSON(URL,source,obamaSaid,romneySaid,pubNo,debateNo)
main()
