import discord
import os
from dotenv import load_dotenv

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$hello'):
    id = message.author.id
    await message.channel.send(id)


client.run(os.getenv("discordToken"))
