import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')

@client.command()
async def hallo(ctx):
    await ctx.send('hallo! het is weer een mooie dag voor het proletariaat!')

@client.command()
async def kapitalisme(ctx):
    await ctx.send('het kapitalisme moet vernietigd worden!')


client.run('NzI5MDMyNDI4NTI5NjQ3NjQ2.XwDCxA.TYZzVhsuTtr2uLhHmM1AFcKssxU')