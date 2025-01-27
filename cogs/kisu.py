import discord
from discord.ext import commands
import os
import random
from datetime import timedelta, datetime
import time

images = os.path.join(os.getcwd(), r"/home/container/data")

def random_image():
    return os.path.join(images, random.choice(os.listdir(images)))

class Kisu(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Kisu cog loaded.')


    @discord.slash_command(
    name="dopamiini",
    description="Ootko tää kissa?"
    )
    async def dopamiini(self, ctx):
        file = discord.File(random_image(), filename="output.jpg")
        embed = discord.Embed(color=0x613613)
        embed.timestamp = datetime.now()
        embed.set_footer(text='Dopamiinia käyttäjälle: ' + ctx.author.name)
        embed.set_image(url="attachment://output.jpg")
        message = await ctx.respond(embed=embed, file=file)
        msg = await message.original_response()
        await msg.add_reaction("💖")


    @discord.slash_command(
    name="pusu",
    description="Pusipusi :3"
    )
    async def pusu(self, ctx, kohde: discord.Option(discord.Member)):
        embed = discord.Embed(color=0x613613)
        embed.timestamp = datetime.now()
        embed.set_footer(text="Pusipusi " + kohde.name + " :3")
        embed.set_image(url="https://media1.tenor.com/m/o7gSaU0fRzwAAAAC/kiss-cat.gif")
        await ctx.respond(embed=embed)

    @discord.slash_command(
    name="gamba",
    description="Heitä kolikkoa"
    )
    async def gamba(self, ctx):
        numero = random.choice([0, 1])
        embed = discord.Embed(color=0x613613)
        embed.timestamp = datetime.now()
        embed.set_footer(text=f"{ctx.author.name} is gambaing")
        embed.set_image(url="https://media1.tenor.com/m/9RsE4H_eUAEAAAAd/coinflip-heads.gif")
        message = await ctx.respond(embed=embed)
        flipmsg = await message.original_response()
        time.sleep(2)
        
        if numero == 1:
            new_embed = discord.Embed(color=0x613613)
            new_embed.timestamp = datetime.now()
            new_embed.set_footer(text="**vine boom sfx**")
            new_embed.set_image(url="https://cdn3.emoji.gg/emojis/4287-middle-finger-cat.png")
            await flipmsg.edit(embed=new_embed)
        else:
            new_embed = discord.Embed(color=0x613613)
            new_embed.timestamp = datetime.now()
            new_embed.set_footer(text="YIPPEE")
            new_embed.set_image(url="https://cdn3.emoji.gg/emojis/9578-thumbs-up-cat.png")
            await flipmsg.edit(embed=new_embed)


def setup(bot):
    bot.add_cog(Kisu(bot))