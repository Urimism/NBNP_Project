import json
import re

# This file is specifically for cleaning the data from IMDB.
# If any new data is scraped this needs to be modified or overhauled completly.


def cleanData(data):
    keys=list(data.keys())


    if (data[keys[2]] is not None): #cleaning raiting
        raiting=data[keys[0]].strip('<span class="AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV">').strip('</span>')
        raiting=float(raiting)
    else:
        raiting = None

    #cleaning title
    clean = re.compile('<.*?>')
    titel=re.sub(clean,'',data[keys[1]])


    if(data[keys[2]] is not None): #cleaning review
        text=(data[keys[2]]).strip('<div>').strip('</div>')
    else:
        text=None
    dataList=[raiting,titel,text]
    return dataList

def getCleanData():
    with open("C:\\Users\\Urim\\Desktop\\projects\\NBP\\recepti\\linksForMovies.json") as f:
        data = json.load(f)
    test = data[3]
    compiledData = list()
    keys = list(test.keys())

    for i in data:
        compiledData.append(cleanData(i))
    celeanedList = list()
    for i in compiledData:
        if (i[0] != None and i[2] is not None):
            celeanedList.append(i)
    return celeanedList



