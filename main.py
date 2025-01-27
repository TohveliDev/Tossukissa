import discord
import asyncio
import config
import os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} online. YIPPEE!")
    print("----------------------------------")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="silly little cats | /help"))

cogfiles = [
    f"cogs.{filename[:-3]}" for filename in os.listdir(r"/home/container/cogs") if filename.endswith(".py")
]

for cogfile in cogfiles:
    try:
        bot.load_extension(cogfile)
    except Exception as err:
        print(err)


@bot.command()
async def syncing(ctx):
    if ctx.author.id == config.OWNERID:
        await bot.sync_commands(force=True, guild_ids=[])
        await ctx.send("YIPPEE")
    else:
        await ctx.send("https://tenor.com/view/cat-nuh-uh-meow-sniff-incorrect-gif-11442321997337963097")

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round (bot.latency * 1000)} ms!')

bot.run(config.TOKEN)
