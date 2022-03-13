import Cleaning as clean
from pymongo import MongoClient
from pprint import  pprint
import certifi
import pymongo
import uuid
import random

def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

if __name__ == '__main__':
    cleanedList=clean.getCleanData()
    #client = pymongo.MongoClient(port=27017)
    #print( client.list_database_names())
    ca = certifi.where()
    client = MongoClient( 'mongodb+srv://Urim:Winterfell1-@cluster0.q6mng.mongodb.net/test',tlsCAFile=ca)
    db = client['MovieReviews']
    movies=db['Movies']

    # oneReview={
    #     "_id":"firstInsertedID",
    #     "attributes":{
    #     "raiting":cleanedList[3][0],
    #     "title":cleanedList[3][1],
    #     "review":cleanedList[3][2]
    #     }
    #
    # }
    # movies.insert_one(oneReview)
    # query={}
    # movies.delete_many(query)

    unique_sequence = uniqueid()
    for entry in cleanedList:
        id=next(unique_sequence)
        id=str(id) + '100'
        id=int(id)
        oneReview = {
            "_id":id,
            "attributes":{
            "raiting":entry[0],
            "title":entry[1],
            "review":entry[2]
            }
        }
        movies.insert_one(oneReview)

    #print(type(str(uuid.uuid4())))
    # query={}
    # movies.delete_many(query)
