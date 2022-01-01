#main.py
import discord
from discord.ext import commands

TOKEN = "TOKEN"
prefix = "r!"

client = commands.Bot(command_prefix=prefix)

@client.command()
async def welcome_msg_send(ctx):
    await ctx.send("Welcome to server")
    print("welcome_msg_send command sended")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")
    print("hello command sended")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, reason=None):
    if reason == None:
        await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
    else:
        messageok = f"You have been banned from ```{ctx.guild.name}``` for ```{reason}```"
        await ctx.send(f"User ```{member}``` has been banned for ```{reason}```")
        await member.send(messageok)
        await member.ban(reason=reason)
        print(f"User {member} has been banned for {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, reason = None):
  if not reason:
      await ctx.send(f"Woah {ctx.author.mention}, Make sure you provide a reason!")
  else:
    messageok = f"You have been kicked from ```{ctx.guild.name}``` for ```{reason}```"
    await ctx.send(f"User ```{member}``` has been banned for ```{reason}```")
    await member.send(messageok)
    await member.kick(reason=reason)
    print(f"User {member} has been kicked for {reason}")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
