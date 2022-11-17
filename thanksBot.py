import discord
from pymongo import MongoClient
import os
from dotenv import load_dotenv
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

  #make shure message isn´t comming from bot
  if message.author == client.user:
    return

  if message.content.startswith('!thanks'):

    author = message.reference.resolved.author
    id = author.id

    collection = dmu.getCollection(db, message)
    
    dmu.incrementScore(collection, id)

    results = collection.find_one({"_id": id})

    await message.channel.send("tack {} nu har du {} poäng" .format(author, results["score"])) 


client.run(os.getenv("discordToken"))
