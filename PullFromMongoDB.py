from pymongo import MongoClient
import certifi


def queryByIndexValue(index):
    ca = certifi.where()
    client = MongoClient('mongodb+srv://Urim:Winterfell1-@cluster0.q6mng.mongodb.net/test', tlsCAFile=ca)
    db = client['MovieReviews']
    movies = db['Movies']

    query = {}
    documents = movies.find(query)
    listOfDataFromMongo = list()

    for i in documents:
        id = i['_id']

        if (id % 1000 == index):
            listOfDataFromMongo.append(i)

    return listOfDataFromMongo

