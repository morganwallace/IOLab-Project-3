import urllib.request, urllib.parse
from time import sleep
import json

def nytimesAPIsearch(query,date):
    endDate = date+1
    url = "http://api.nytimes.com/svc/search/v1/article?format=json&query="+query+"&begin_date="+str(date)+"&end_date="+str(endDate)+"&api-key=28e0d1a82dd11796e597dad020485930:2:66919397"
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    urls = []
    for i in results['results']:
        urls.append(i['url'])
    return urls

#counts the lines in the 'jsonFile' file so the JSON variable can have the correct ID
def countInFile(jsonFile):
    try: file =  open(jsonFile,"r")
    else:
        file =  open(jsonFile,"w")
        file.close()
        file =  open(jsonFile,"r")
    counter = 0
    for line in file: counter +=1
    return counter

#Export to 'data.js' for sentiment analysis
def saveJSON(JSONdata):
    jsFile = open(jsonFile,'a')
    jsFile.write(JSONdata+'\n')
    jsFile.close()

def main(date):
    jsonNo = countInFile(jsonFile)+1 #initiates a new ID for JSON entries.
    #debateNo
    debateNo = "1"
    if  20121014 < date <20121021: debateNo = "2"
    elif date >= 20121021: debateNo = "3"   
    #end debateNo
    
    searchResults=nytimesAPIsearch("obama+romney+presidential+debate",date)[:2]
    print(searchResults)

    for url in searchResults:
        jsonName = "var s"+str(jsonNo)+" = {'publication':'"+newspaper+"','date':'"+str(date)+"','url':'"+url+"','debate':'"+debateNo+"'};"
        saveJSON(jsonName)

jsonFile = "data2.js"
newspaper = 'NY Times'

for date in range(20121003,20121004):
    main(date)#run for october dates
for date in range(20121101,20121106):
    main(date)#run for November Dates

