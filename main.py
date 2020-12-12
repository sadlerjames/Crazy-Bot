#import required dependicies
import discord
from discord.ext import commands

#import Discord Token
from token import TOKEN 

description = '''I am the Craziest Bot of them all!'''
bot = commands.Bot(command_prefix='!crazy', description=description, help_command=None)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am Crazy Bot, what can I do for you today?")

@bot.command()
async def help(ctx):
    await ctx.send("""
    Need help? No problem, I hear to assit you with all your needs.

    What clever things am I able to do? Well not much but let me show you:    
    """)



bot.run(TOKEN)