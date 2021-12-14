
#main.py
import discord
from discord.ext import commands

TOKEN = "TOKEN"
prefix = "r!"

client = commands.Bot(command_prefix=prefix)

@client.command()
async def welcome_msg_send(ctx):
    await ctx.send("Welcome to server")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)
