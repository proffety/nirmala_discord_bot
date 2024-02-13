import discord
import json

with open("config.json", "r") as f:
    data = json.load(f)

token = data["token"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/kelvin'):
        await message.channel.send('macaco')

client.run(token)