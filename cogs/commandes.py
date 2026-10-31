import random
from discord.ext import commands

class CommandesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx):
        result = random.randint(1, 6)
        await ctx.send(f'{ctx.author.name} lance un dé et obtient : {result}')

async def setup(bot):
    await bot.add_cog(CommandesCog(bot))