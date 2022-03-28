import discord, os, keep_alive, asyncio, datetime, pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix=':',
  self_bot=True
)



@client.event
async def on_connect():
  await client.change_presence(status = discord.Status.online) //Change your presence status by ''discord.Status.online, discord.Status.dnd, discord.Status.idle'' 


keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
