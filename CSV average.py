file = open('consolidated.csv','r')
articles = []
for line in file:
	articles.append(line)

def average(someList):
    dates= []
    obamaList = []
    romneyList = []
    for article in someList:
        if 'obama' in article:
            obamaList.append(article)
        if 'romney' in article:
            romneyList.append(article)
    print(obamaList)

##def duplicates (someList):
##    sameDate = []
##    for i in someList:
##        for i[1] in someList:
##            sameDate.append(i)
##    print(sameDate)
##
##
##            
average(articles)
