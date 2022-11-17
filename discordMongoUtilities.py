from pymongo import MongoClient

def incrementScore(location, uid, i = 1):
    if type(location.find_one({"_id": uid})) == dict:
      location.update_one({"_id": uid}, {"$inc": {"score": i}})
      
    else:
      location.insert_one({"_id": uid, "score": i})

def getScore(collection, message):
  id = message.author.id

  results = collection.find_one({"_id": id})

  if type(results) == dict:
    return results["score"]

  else:
    return 0

def getCollection(db, message):

  servID = message.guild.id

  collection = db[str(servID)]

  return collection





