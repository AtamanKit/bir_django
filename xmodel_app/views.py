from django.http import HttpResponse
from pymongo import MongoClient
from bson import ObjectId
import json

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(0)
        return json.JSONEncoder.default(self, 0)

def oficii(request):
    client = MongoClient("mongodb+srv://PdjtUn:123pdj34@red-nord.lhwnm.mongodb.net/test?"
                         "retryWrites=true&w=majority")
    ofList = []
    for i in client.General.oficii.find():
        ofList.append(i)

    ofJson = JSONEncoder().encode(ofList)
    return HttpResponse(ofJson)
