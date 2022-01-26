#bot.py

import discord
from discord.ext import commands

import sys

TOKEN = "ODk5NjExMzcyNjk3MDMwNjg2.YW1SYQ.68iTCU00SzYZCFT2fekPQ2ZE2zw"
prefix = "r!"

client = commands.Bot(command_prefix=prefix)

@client.command()
async def welcome_msg_send(ctx):
    try:
        await ctx.send("Welcome to server")
        print("welcome_msg_send command sended")
    except Exception as error:
        await ctx.send(error)
        print(f"{error}")

@client.command()
async def hello(ctx):
    try:
        await ctx.send("Hello")
        print("hello command sended")
    except Exception as error:
        await ctx.send(error)
        print(f"{error}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, make sure you provide a reason!")
        print(f"Woah {ctx.author.mention}, make sure you provide a reason!")
    else:
        try:
            messageok = f"You have been kicked from `{ctx.guild.name}` for `{reason}`"
            await ctx.send(f"User `{member}` has been kicked for `{reason}`")
            await member.send(messageok)
            await member.kick(reason=reason)
            print(f"User {member} has been kicked for {reason}")
        except Exception as error:
            await ctx.send(error)
            print(f"{error}")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, make sure you provide a reason!")
        print(f"Woah {ctx.author.mention}, make sure you provide a reason!")
    else:
        try:
            messageok = f"You have been banned from `{ctx.guild.name}` for `{reason}`"
            await ctx.send(f"User `{member}` has been banned for `{reason}`")
            await member.send(messageok)
            await member.ban(reason=reason)
            print(f"User {member} has been banned for {reason}")
        except Exception as error:
            await ctx.send(error)
            print(f"{error}")


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

if __name__ == "__main__":
    try:
        client.run(TOKEN)
        on_ready()
    except KeyboardInterrupt:
        print("\n\nKeyboardInterrupt > > > Exiting...")
        sys.exit(0)
