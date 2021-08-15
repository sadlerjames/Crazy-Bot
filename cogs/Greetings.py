import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os


class Greetings(commands.Cog):

    def __init__(self, client):
        self.client = client

    #hello
    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, I am Crazy Bot. I may not do much at the moment, but I will do in the future.")

    #user leaving
    @commands.Cog.listener()
    async def on_member_remove(member):
        channel = client.get_channel(801151337306914889)
        await channel.send("Goodbye")

def setup(client):
    client.add_cog(Greetings(client))