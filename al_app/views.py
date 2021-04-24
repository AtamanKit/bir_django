from django.http import HttpResponse
from pymongo import MongoClient
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(0)
        return json.JSONEncoder.default(self, 0)

def al(request):
    client = MongoClient("mongodb+srv://PdjtUn:123pdj34@red-nord.lhwnm.mongodb.net/test?"
                         "retryWrites=true&w=majority")
    myList = []
    for i in client.djUN_test.al_2021_04.find():
        myList.append(i)

    myJson = JSONEncoder().encode(myList)
    return HttpResponse(myJson)
