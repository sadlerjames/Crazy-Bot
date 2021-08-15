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

    #event
    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        if ("meme" or "Meme" or "MEME") in message.content:
            await message.channel.send("Did someone say meme?")
            #send meme inside embed message
            embed = discord.Embed(title="")
            embed.set_image(url="https://c.tenor.com/jItxRf-KWosAAAAC/jeffrey-dean-morgan-smile.gif")
            await message.channel.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))


