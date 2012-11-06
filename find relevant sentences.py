#Exports JSON with Obama Sentences and Romney Sentences

import json
import os

article = input("paste the language of the article here: ")
source = input("Newspaper: ")
debateNo = input("Debate number: ")
URL = input("url: ")
obamaSentences= []
romneySentences= []

#find sentences with obama or romney in it
def findInSentences(articleText):
    allSentences=articleText.split('.')
    for i in article.split('.'):
        if 'Romney' in i:
            i.strip('\\')
            i.strip('\n')#remove whitespace
            romneySentences.append(i)
        if 'Obama' in i:
            i.strip('\\')
            i.strip('\n')#remove whitespace
            obamaSentences.append(i)
    
#Export for sentiment analysis
def formatJSON(sentences,fileName,URL):
    jsonObj = {"sentences":str(sentences)[1:-1],'source':URL}
    jsonFile = open(fileName,'w')#saves file outside of github repo        
    json.dump(jsonObj,jsonFile)
    jsonFile.close()
    print('Saved here:',fileName)
    return jsonObj

def naming(fileName):
    fileName +='.json'#give extension
    fileName = os.path.join('JSON',fileName)#put in folder called 'JSON'
    counter = 0
    while os.path.exists(fileName):
        counter+=1
        if counter<=1:
            fileName=fileName[:-5]+"("+str(counter)+")"+fileName[-5:]
        else:
            fileName[-7]=str(counter)
    return fileName


def main():
    findInSentences(article)
    if obamaSentences: #if there were mentions of Obama
        formatJSON(obamaSentences,naming('Obama, '+source+" - debate no "+debateNo),URL)
    if romneySentences:#if there were mentions of Romney
        formatJSON(romneySentences,naming('Romney, '+source+" - debate no "+debateNo),URL)
main()
