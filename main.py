from nextcord.ext import commands
import nextcord
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = nextcord.Intents.all()
client = commands.Bot(intents=intents, command_prefix="s!")


@client.event
async def on_ready():
    print(f"Logged in as {client.user}.")


@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error: {error}")


# ?    _____ ____   _____  _____
# ?   / ____/ __ \ / ____|/ ____|
# ?  | |   | |  | | |  __| (___
# ?  | |   | |  | | | |_ |\___ \
# ?  | |___| |__| | |__| |____) |
# ?   \_____\____/ \_____|_____/


for fn in os.listdir("./cogs"):
    if fn.endswith(".py"):
        client.load_extension(f"cogs.{fn[:-3]}")


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension}.")


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}.")


@client.command()
async def reload(ctx, extension):
    client.reload_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}.")


# ?    _____ ____   _____  _____
# ?   / ____/ __ \ / ____|/ ____|
# ?  | |   | |  | | |  __| (___
# ?  | |   | |  | | | |_ |\___ \
# ?  | |___| |__| | |__| |____) |
# ?   \_____\____/ \_____|_____/


client.run(TOKEN)
