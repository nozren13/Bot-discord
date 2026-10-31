import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

class MonBot(commands.Bot):
    async def setup_hook(self):
        for extension in ['commandes']:
            await self.load_extension(f'cogs.{extension}')

intents = discord.Intents.all()
bot = MonBot(command_prefix="/", intents = intents)

@bot.event
async def on_ready():
  print(f"Connecté en tant que {bot.user}")
  try:
    synced = await bot.tree.sync()
    print(f"{len(synced)} commande(s) synchronisée(s)")
  except Exception as e:
    print(e)

bot.run(token)