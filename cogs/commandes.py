import random
import discord
from discord import app_commands
from discord.ext import commands

class CommandesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="roll")
    async def roll(self, interaction: discord.Interaction):
        result = random.randint(1, 6)
        await interaction.response.send_message(f'{interaction.user.name} lance un dé et obtient : {result}')

async def setup(bot):
    await bot.add_cog(CommandesCog(bot))