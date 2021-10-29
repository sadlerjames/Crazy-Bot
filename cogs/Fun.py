import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import json
import os


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    #listen for words
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        if ("meme" or "Meme" or "MEME") in message.content:
            await message.channel.send("Did someone say meme?")
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/jItxRf-KWosAAAAC/jeffrey-dean-morgan-smile.gif")
            await message.channel.send(embed=embed)

        if ("spiderman" or "peter-parker" or "peter parker" or "spider-man" or "spider man" or "tobey maguire" or "tobey" or "tobeymaguire") in message.content:
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/P8VsDwHZreYAAAAd/tobey-maguire-spider-man.gif")
            await message.channel.send(embed=embed)

        if ("fuck") in message.content:
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/Rt5-pEJHt04AAAAC/fuck-damn.gif")
            await message.channel.send(embed=embed)

        if ("game") in message.content:
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/xtp2N6fg2SwAAAAC/stickergiant-game-time.gif")
            await message.channel.send(embed=embed)
        
        if ("sorry") in message.content:
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/B1ooFF-GRUMAAAAd/no-apology-necessary-travis.gif")
            await message.channel.send(embed=embed)

        


def setup(client):
    client.add_cog(Fun(client))


