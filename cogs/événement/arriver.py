import discord
import io
from PIL import Image, ImageDraw
from discord.ext import commands

class ArriverCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def circle_avatar(self, member : discord.Member):
        filename = f"{member.name}.png"
        path_user = f"./images/avatars/"+filename
        await member.display_avatar.replace(size=128, format="png").save(path_user)

        user_avatar =  Image.open(path_user).convert("RGBA")

        width, height = user_avatar.size
        size = min(width, height)

        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)

        draw.ellipse((0, 0, size, size), fill=255)

        left = (width - size) // 2
        top = (height - size) // 2
        right = left + size
        bottom = top + size
        avatar = user_avatar.crop((left, top, right, bottom))

        avatar.putalpha(mask)

        avatar.save(path_user, 'PNG')

    async def image_arriver(self, ):
        # J'en suis ici
        # Je sais pas si je dois récupérer l'image par la fonction ou par le module 'Image' 
        return

    @commands.Cog.listener()
    async def on_member_join(self, member : discord.Member):
        avatar = await self.circle_avatar(member)

        channel = member.guild.get_channel(1562765027327483934)

        await channel.send(file=avatar)
        return

async def setup(bot):
    await bot.add_cog(ArriverCog(bot))