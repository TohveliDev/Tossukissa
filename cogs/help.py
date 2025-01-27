import discord
from discord.ext import commands
from datetime import timedelta, datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Help cog loaded.')


    @discord.slash_command(
    name="help",
    description="Mitä, miten ja missä?"
    )
    async def Help(self, ctx):
        embed = discord.Embed(title="Help", description="Tossukissan commandit",color=0x613613)
        embed.add_field(name="/dopamiini", value="Lähettää kissakuvan :3", inline=False)
        embed.add_field(name="/pusu (käyttäjä)", value="Lähettää pusun käyttäjälle :3", inline=False)
        embed.add_field(name="/gamba", value="Heittää kolikkoa", inline=False)
        embed.add_field(name="/help", value="Kaikki Tossukissan commandit", inline=False)
        embed.add_field(name="/info", value="Botin perusinfo", inline=False)
        embed.timestamp = datetime.now()
        embed.set_footer(text=ctx.author.name)
        await ctx.respond(embed=embed)


    @discord.slash_command(
    name="info",
    description="Kuka, ketä ja kenen?"
    )
    async def Info(self, ctx):
        embed = discord.Embed(title="Info", color=0x613613)
        embed.add_field(name="Dev", value="mizuzyn", inline=True)
        embed.add_field(name="Version", value="1.0.3", inline=True)
        embed.add_field(name="Prefix", value="/", inline=True)
        embed.timestamp = datetime.now()
        embed.set_footer(text=ctx.author.name)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))