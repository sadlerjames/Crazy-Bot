import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @kick.error
    async def kick_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to kick people!")


    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned')

    @ban.error
    async def ban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to ban people!")

    @commands.command()
    @has_permissions(administrator=True)
    async def unban(ctx, member: discord.Member, *, reason=None):
        #not being run for somereason
        banned_users = await ctx.guild.bans()
        print(banned_users)
        member_name, member_discriminator = member.split("#")
        print(member_name)

        for ban_entry in banned_users:
            print(ban_entry)
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned {user.mention}')
                return

    @unban.error
    async def unban_error(ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permission to ban people!")

    @commands.command()
    async def manualWelcomeUser(ctx, user:discord.Member, *, message=None):
        message = "Welcome to the CrazyBoy server! It's great to have you here!"
        embed = discord.Embed(title=message)
        await user.send(embed=embed)

    @commands.command()
    async def embed(ctx):
        embed = discord.Embed(title="Dog", url="https://google.com", description="We love dogs!", color=0x4dff4d)
        embed.set_author(name=ctx.author.display_name, url="https://instagram.com/james.d.s_/", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.pixabay.com/photo/2016/10/22/17/46/mountains-1761292_960_720.jpg")
        embed.add_field(name="Labradore", value="Cute dogs", inline=True)
        embed.add_field(name="Pugs", value="Cute dogs", inline=True)
        embed.set_footer(text="Thank you for reading")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Admin(client))