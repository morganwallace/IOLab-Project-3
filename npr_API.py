import urllib.request, urllib.parse
import json

def NPRsearch(query,date):
    day = str(date)[-2:]
    month = str(date)[4:-2]
    year = str(date)[:4]
    url = "http://api.npr.org/query?searchTerm=Obama+Romney+Presidential+Debate&meta=none&output=JSON&sort=relevance&date="+month+"%2F"+day+"%2F"+year+"&apikey=MDEwNDEzMDMxMDEzNTI4NDE5MzliNDk4MA001"
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    urls = []
    for story in results['list']['story']:
        for link in story['link']:
            if link['type']=='html': urls.append(link["$text"])
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


jsonFile = "data3.js"
newspaper = 'NY Times'
jsonNo = countInFile(jsonFile)+1 #initiates a new ID for JSON entries.

def main(date):
    jsonNo = countInFile(jsonFile)+1
    debateNo = "1"
    if  20121014 < date <20121021: debateNo = "2"
    elif date >= 20121021: debateNo = "3"   
    
    searchResults=NPRsearch("obama+romney+presidential+debate",date)[:2]
    print(searchResults)

    for url in searchResults:
        jsonName = "var s"+str(jsonNo)+" = {'publication':'"+newspaper+"','date':'"+str(date)+"','url':'"+url+"','debate':'"+debateNo+"'};"
        saveJSON(jsonName)
        jsonNo+=1


for date in range(20121003,20121031):
    main(date)#run for october dates

for date in range(20121101,20121106):
    main(date)#run for November Dates
