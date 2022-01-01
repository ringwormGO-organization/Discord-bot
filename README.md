# Discord-bot
Discord bot for ringwormGO written in Python

# Invite bot in own server
https://discord.com/api/oauth2/authorize?client_id=899611372697030686&permissions=8&scope=bot

NOTE: Bot is currently not 24h active.

# How to use?
### Open the dir in vs code.
### Open an new terminal in the folder (vs code or linux/windows terminal)
### In the terminal, type: 
```bash
python3 -v
```
### It will return something like (3.1.3), if the first number is 3, then you can continue. Or else, uninstall the python installation and install python 3. If it returns an error, it means that you dont have python, so you will have to install python.
### After installing the correct version of python, do:
```bash
pip3 install discord.py
```
### After this, make a bot on discord and add it to your server, there are a lot of tutorials on the internet on how to do this. Copy the bot token and replace "TOKEN" with the token
### Now, go cd into the bot dir and run
```bash
python3 bot.py
```
### Now the bot should be online!!

# Bot in action (pictures)
![107](https://user-images.githubusercontent.com/83548580/147858174-cb7c4844-54c9-4891-ae21-14b4c2e51e36.jpg)
![110](https://user-images.githubusercontent.com/83548580/147858270-15c3f41d-0dc1-48fd-a9e6-22dd1f0732be.jpg)

# Bot in action (terminal log)

*Command Prompt - Windows 11 Pro*

This log is from long period of runnig bot (10 minutes).

About 5 messages to bot are sended.

```
E:\AndrejBackup\Andrej\PRIVATNO-duboko\Ostali\RingwormGo\RingwormGO\Andrej\DISCORD>python bot.py
ringwormGO Bot#6927 has connected to Discord!
Ignoring exception in command kick:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 855, in invoke
    await self.prepare(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 777, in prepare
    if not await self.can_run(ctx):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1087, in can_run
    return await discord.utils.async_all(predicate(ctx) for predicate in predicates)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\utils.py", line 348, in async_all
    for elem in gen:
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1087, in <genexpr>
    return await discord.utils.async_all(predicate(ctx) for predicate in predicates)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1790, in predicate
    raise MissingPermissions(missing)
discord.ext.commands.errors.MissingPermissions: You are missing Kick Members permission(s) to run this command.
Ignoring exception in command kick:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 85, in wrapped
    ret = await coro(*args, **kwargs)
  File "E:\AndrejBackup\Andrej\PRIVATNO-duboko\Ostali\RingwormGo\RingwormGO\Andrej\DISCORD\bot.py", line 40, in kick
    await member.send(messageok)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\abc.py", line 1013, in send
    channel = await self._get_channel()
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\member.py", line 299, in _get_channel
    ch = await self.create_dm()
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\member.py", line 142, in general
    return await getattr(self._user, x)(*args, **kwargs)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\user.py", line 764, in create_dm
    data = await state.http.start_private_message(self.id)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\http.py", line 254, in request
    raise HTTPException(r, data)
discord.errors.HTTPException: 400 Bad Request (error code: 50007): Cannot send messages to this user

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 863, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 94, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: HTTPException: 400 Bad Request (error code: 50007): Cannot send messages to this user
User Andro#4771 has been kicked for Test
Ignoring exception in command ban:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 855, in invoke
    await self.prepare(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 777, in prepare
    if not await self.can_run(ctx):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1087, in can_run
    return await discord.utils.async_all(predicate(ctx) for predicate in predicates)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\utils.py", line 348, in async_all
    for elem in gen:
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1087, in <genexpr>
    return await discord.utils.async_all(predicate(ctx) for predicate in predicates)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 1790, in predicate
    raise MissingPermissions(missing)
discord.ext.commands.errors.MissingPermissions: You are missing Ban Members permission(s) to run this command.
Ignoring exception in command ban:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 855, in invoke
    await self.prepare(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 789, in prepare
    await self._parse_arguments(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 697, in _parse_arguments
    transformed = await self.transform(ctx, param)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 542, in transform
    raise MissingRequiredArgument(param)
discord.ext.commands.errors.MissingRequiredArgument: member is a required argument that is missing.
Ignoring exception in command ban:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 855, in invoke
    await self.prepare(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 789, in prepare
    await self._parse_arguments(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 697, in _parse_arguments
    transformed = await self.transform(ctx, param)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 542, in transform
    raise MissingRequiredArgument(param)
discord.ext.commands.errors.MissingRequiredArgument: member is a required argument that is missing.
Ignoring exception in command None:
discord.ext.commands.errors.CommandNotFound: Command "kick3" is not found
Ignoring exception in command kick:
Traceback (most recent call last):
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 855, in invoke
    await self.prepare(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 789, in prepare
    await self._parse_arguments(ctx)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 697, in _parse_arguments
    transformed = await self.transform(ctx, param)
  File "C:\Users\vangu\AppData\Local\Programs\Python\Python310\lib\site-packages\discord\ext\commands\core.py", line 542, in transform
    raise MissingRequiredArgument(param)
discord.ext.commands.errors.MissingRequiredArgument: member is a required argument that is missing.
hello command sended
welcome_msg_send command sended
hello command sended
hello command sended
```
