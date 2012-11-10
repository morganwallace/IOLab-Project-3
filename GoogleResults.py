##This code will query Google for Presidential Debate related newspaper articles and return URLs for the top hits.
#Results are saved in JSON format in 'data.js'

#Program written by Morgan Wallace

#!/usr/bin/python3
import json
import urllib.request, urllib.parse
from time import sleep


def GoogleSearch(searchfor):
    query = urllib.parse.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    data = results['responseData']
    print("Searching Google for: " + searchfor)
    try:
        hits = data['results']
        urls = []
        for h in hits: urls.append(h['url'])
        return urls[:2] #return the first 2 links
    except: return []

jsonFile = "data2.js"

#counts the lines in the 'jsonFile' file so the JSON variable can have the correct ID
def countInFile():
    file =  open(jsonFile,"r")
    counter = 0
    for line in file: counter +=1
    return counter

#Export to 'data.js' for sentiment analysis
def saveJSON(JSONdata):
    jsFile = open(jsonFile,'a')
    jsFile.write(JSONdata+'\n')
    jsFile.close()

##############
    #modify this information for queries.
newspapers = ['latimes.com','washingtonpost.com']
debateDates = ['October 16','October 17','October 22','October 23']
#############

months = {'October':"10","November":"11"} #used later to reformat the date
jsonNo = countInFile()+1 #initiates a new ID for JSON entries.

print("The following has been appended to 'data.js':\n")
for newspaper in newspapers:
    for date in debateDates:
        query = newspaper + ' Obama Romney Presidential debate ' + date
        urls = GoogleSearch(query)
        if urls: #if Google search results were returned
            spaceLoc = date.find(" ")
            date = int("2012"+months[date[:spaceLoc]]+date[spaceLoc+1:])
            debateNo = "1"
            if  20121014 < date <20121021: debateNo = "2"
            elif date >= 20121021: debateNo = "3"           
            for url in urls:
                jsonName = "var s"+str(jsonNo)+" = {'publication':'"+newspaper+"','date':'"+str(date)+"','url':'"+url+"','debate':'"+debateNo+"'};"
                saveJSON(jsonName)
                print(jsonName)
                jsonNo +=1
                sleep(2)
        else: print("No URLs were found for the query: "+ query)

