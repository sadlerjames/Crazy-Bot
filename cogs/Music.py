import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client


    queues = {}

    def check_queue(ctx, id):
        if queues[id] != []:
            voice = ctx.guild.voice_client
            source = queues[id].pop(0)
            player = voice.play(source)

    @commands.command(pass_context = True)
    async def join(self, ctx):
        if (ctx.author.voice):
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('piano.wav')
            player = voice.play(source)

        else:
            await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")


    @commands.command(pass_context = True)
    async def leave(self, ctx):
        if (ctx.voice_client):
            await ctx.guild.voice_client.disconnect()
            await ctx.send("I left the voice channel")
        else:
            await ctx.send("I am not in a voice channel")


    @commands.command(pass_context = True)
    async def pause(self, ctx):
        voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await ctx.send("At the moment, there is no audio playing in the voice channel!")

    @commands.command(pass_context = True)
    async def resume(self, ctx):
        voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await ctx.send("At the moment, no song is paused!")

    @commands.command(pass_context = True)
    async def stop(self,ctx):
        voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
        voice.stop()

    @commands.command(pass_context = True)
    async def play(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = arg + '.wav'
        source = FFmpegPCMAudio("./audio/" + song)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

    @commands.command(pass_context = True)
    async def queue(self, ctx, arg):
        voice = ctx.guild.voice_client
        song = arg + '.wav'
        source = FFmpegPCMAudio("./audio/" + song)

        guild_id = ctx.message.guild.id

        if guild_id in queues:
            queues[guild_id].append(source)

        else:
            queues[guild_id] = [source]

        await ctx.send("Added to queue")

def setup(client):
    client.add_cog(Music(client))