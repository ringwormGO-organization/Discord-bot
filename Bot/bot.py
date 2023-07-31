import hikari
import lightbulb

import os
import sys

import helper

USE_REPL = False
USE_COLORS = True
bot = None

if USE_REPL == False:
    bot = lightbulb.BotApp(
        token="TOKEN",
        default_enabled_guilds="SERVER_ID (needs to be interger)"
    )

else:
    bot = lightbulb.BotApp(
        token=os.environ['TOKEN'],
        default_enabled_guilds=int(os.environ['SERVER_ID'])
    )

@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print("Bot has has connected to Discord!")

@bot.command
@lightbulb.command('hello', 'Says hello!')
@lightbulb.implements(lightbulb.SlashCommand)
async def hello(ctx):
    await ctx.respond(f'Hello!')
    helper.log("Hello command sent", USE_COLORS, "green")

@bot.command
@lightbulb.command('help', 'Sends a list of commands!')
@lightbulb.implements(lightbulb.SlashCommand)
async def help(ctx):
    sorted_commands = sorted(helper.bot_commands)
    await ctx.respond(f'{sorted_commands}')
    helper.log("help command sent", USE_COLORS, "green")
    helper.log(f"{sorted_commands}", USE_COLORS, "white")

@bot.command
@lightbulb.option('num1', 'First number', type=int)
@lightbulb.option('num2', 'Second number', type=int)
@lightbulb.command('add', 'Sums two numbers!')
@lightbulb.implements(lightbulb.SlashCommand)
async def calc(ctx):
    await ctx.respond(f'Result is: {ctx.options.num1 + ctx.options.num2}')
    helper.log("calc command sent", USE_COLORS, "green")
    helper.log(f'Result is: {ctx.options.num1 + ctx.options.num2}', USE_COLORS, "white")

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
    helper.log("User has been banned!", USE_COLORS, "green")

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
    helper.log("User has been kicked!", USE_COLORS, "green")

if __name__ == "__main__":
    try:
        if USE_REPL == True:
            from keep_alive import keep_alive
            keep_alive()
            bot.run()
        
        else:
            bot.run()
    except Exception as e:
        print(f"Exception caught: {e}")
        print("Exiting...")
        sys.exit(0)
