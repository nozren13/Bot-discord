import discord
from discord.ext import commands

class ArriverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        avatar = member.avatar
        channel = member.guild.get_channel(1562765027327483934)

        await channel.send(avatar)
        return

async def setup(bot):
    await bot.add_cog(ArriverCog(bot))