import discord
from discord.ext import commands
import os

# خُد التوكن من متغير بيئي
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready!')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm alive.")

bot.run(TOKEN)
