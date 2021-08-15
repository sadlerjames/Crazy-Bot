import discord
from discord.ext import commands
import os

#import Bot Token
from apikeys import *

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '?', intents=intents)

@client.event
async def on_ready():
    print("The bot is now ready for use!")
    print("------------------------------")

    #send a message to server
    channel = client.get_channel(745026098001215540)
    await channel.send("I've just had a good sleep, recharged the batteries and I'm now back online now")
    #send meme inside embed message
    embed = discord.Embed(title="")
    embed.set_image(url="https://c.tenor.com/FI_r4cjN7w4AAAAC/bear-dance.gif")

    await channel.send(embed=embed)


initial_extensions = []

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(extension)

client.run(BOTTOKEN)