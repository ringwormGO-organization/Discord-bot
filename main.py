import os
import sys

import colorama
from dotenv import load_dotenv
import hikari
import lightbulb

bot_commands = ['add', 'ban', 'hello', 'help', 'kick']
load_dotenv()

token = os.getenv("TOKEN")
server_id_tuple = os.getenv("SERVER_ID").split(",")

bot = lightbulb.BotApp(
    token=token,
    default_enabled_guilds=server_id_tuple
)

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has has connected to Discord!")

@bot.command
@lightbulb.command('hello', 'Says hello!')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond(f'Hello!')
    print(colorama.Fore.LIGHTCYAN_EX + "Hello command sent" + colorama.Fore.RESET)

@bot.command
@lightbulb.command('help', 'Sends a list of commands!')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    sorted_commands = sorted(bot_commands)
    await ctx.respond(f'{sorted_commands}')
    print(colorama.Fore.LIGHTCYAN_EX + "Help command sent" + colorama.Fore.RESET)
    print(colorama.Fore.WHITE + f"{sorted_commands}" + colorama.Fore.RESET)

@bot.command
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.option('num2', 'Second number', type=int)
@lightbulb.command('add', 'Sums two numbers!')
@lightbulb.implements(lightbulb.SlashCommand)
async def calc(ctx):
    await ctx.respond(f'Result is: {ctx.options.num1 + ctx.options.num2}')
    print(colorama.Fore.LIGHTCYAN_EX + "Calc command sent" + colorama.Fore.RESET)
    print(colorama.Fore.WHITE + f'Result is: {ctx.options.num1 + ctx.options.num2}' + colorama.Fore.RESET)

@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.BAN_MEMBERS))
@lightbulb.option("reason", "Reason for the ban", required=False)
@lightbulb.option("user", "The user to ban.", type=hikari.User)
@lightbulb.command("ban", "Ban a user from the server.")
@lightbulb.implements(lightbulb.SlashCommand)
async def ban(ctx: lightbulb.SlashContext) -> None:
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a guild.")
        return

    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
    await ctx.app.rest.ban_user(ctx.guild_id, ctx.options.user.id, reason=ctx.options.reason or hikari.UNDEFINED)
    await ctx.respond(f"Banned {ctx.options.user.mention}.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")

    print(colorama.Fore.LIGHTCYAN_EX + "User has been banned!" + colorama.Fore.RESET)

@bot.command()
@lightbulb.add_checks(lightbulb.has_guild_permissions(hikari.Permissions.KICK_MEMBERS))
@lightbulb.option("reason", "Reason for the kick", required=False)
@lightbulb.option("user", "The user to kick.", type=hikari.User)
@lightbulb.command("kick", "Kick a user from the server.")
@lightbulb.implements(lightbulb.SlashCommand)
async def kick(ctx: lightbulb.SlashContext) -> None:
    if not ctx.guild_id:
        await ctx.respond("This command can only be used in a guild.")
        return

    await ctx.respond(hikari.ResponseType.DEFERRED_MESSAGE_CREATE)
    await ctx.app.rest.kick_user(ctx.guild_id, ctx.options.user.id, reason=ctx.options.reason or hikari.UNDEFINED)
    await ctx.respond(f"Kicked {ctx.options.user.mention}.\n**Reason:** {ctx.options.reason or 'No reason provided.'}")

    print(colorama.Fore.GREEN + "User has been kicked!" + colorama.Fore.RESET)

if __name__ == "__main__":
    try:
        bot.run()
    except Exception as e:
        print(f"Exception caught: {e}")
        print("Exiting...")
        
        sys.exit(0)
