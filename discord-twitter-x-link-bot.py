import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")
PREFIX = os.environ.get("PREFIX")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.event
async def on_message(message: discord.Message):
    # Check if the message author is not a bot
    if message.author.bot:
        return

    # Replace twitter.com links
    if "twitter.com" in message.content:
        content = message.content.replace("twitter.com", "twittpr.com")

        # Delete the original message
        await message.delete()

        # Mention the original poster's name silently in the modified message
        modified_message = f"{message.author.mention} Here is the modified message:\n{content}"
        await message.channel.send(modified_message)

    # Replace x.com links
    if "x.com" in message.content:
        content = message.content.replace("x.com", "fixupx.com")

        # Delete the original message
        await message.delete()

        # Mention the original poster's name silently in the modified message
        modified_message = f"{message.author.mention} Here is the modified message:\n{content}"
        await message.channel.send(modified_message)

    # Allow commands to be processed as well
    await bot.process_commands(message)

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("Pong!")

bot.run(TOKEN)