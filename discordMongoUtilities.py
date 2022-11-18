from pymongo import MongoClient

def incrementScore(location, uid, i = 1):
  """Increment score of user or if it does not exist makes a document"""

  if type(location.find_one({"_id": uid})) == dict:
    location.update_one({"_id": uid}, {"$inc": {"score": i}})
      
  else:
    location.insert_one({"_id": uid, "score": i})

def getScore(location, message):
  """Returns the user score. Takes two arguments collection and message"""

  id = message.author.id

  results = location.find_one({"_id": id})

  if type(results) == dict:
    return results["score"]

  else:
    return 0

def getCollection(db, message):
  """Returns collection for server. If colection doesn't exist it makes a collection"""

  servID = message.guild.id

  collection = db[str(servID)]

  return collection





