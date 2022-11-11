from pymongo import MongoClient

def incrementScore(location, uid, i = 1):
    if type(location.find_one({"_id": uid})) == dict:
      location.update_one({"_id": uid}, {"$inc": {"score": i}})
    else:
      location.insert_one({"_id": uid, "score": i})
