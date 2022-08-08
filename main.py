import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix="$")

print('TOKEN')
print(os.getenv('TOKEN'))

@client.command()
async def hello(ctx):
    await ctx.send('OIIII')
    print('FUNCIONOU')

@client.command()
async def start_game(ctx, arg1):
    id = int(arg1.replace('@','').replace('<', '').replace('>', ''))
    user = await client.fetch_user(id)
    await user.send('FOIIIIIIIIIIIIIIIII')

@client.event
async def on_ready():
    print(f'{client.user}')
    print('INICIOU')

@client.command()
async def send_dm(ctx, content='Hello' ):
    print('printa')
    print(ctx.author)
    await ctx.author.send(content)

client.run(os.getenv('TOKEN'))
