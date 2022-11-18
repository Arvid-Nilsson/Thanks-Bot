import os
import discord
from dotenv import load_dotenv
from pymongo import MongoClient
import discordMongoUtilities as dmu

load_dotenv()

#Setting discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

#logging into database
cluster = MongoClient(os.getenv('CLUSTER'))

db = cluster.thanksBot

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):

  #Make shure message isn´t comming from bot
  if message.author == client.user:
    return

  if message.content.startswith('!thanks'): 

    collection = dmu.getCollection(db, message)

    #Give user their points if they write !thanks get score
    if "get score" in message.content.lower():
      results = dmu.getScore(collection, message)

      await message.channel.send(f"Du har {results} poäng")

    #Give instructional text if user writes !thanks help
    elif "help" in message.content.lower():
      with open("Help.txt") as f:
        content = f.read()

        await message.channel.send(content)

    #Give the author of the replied to message points for helping
    else:
      #Making shure that the message is a reply
      try:
        author = message.reference.resolved.author
      except:
        return
        
      id = author.id

      dmu.incrementScore(collection, id)

      results = collection.find_one({"_id": id})

      await message.channel.send("Tack {} nu har du {} poäng" .format(author, results["score"])) 


#Run bot
if __name__ == "__main__":
  client.run(os.getenv("discordToken"))
