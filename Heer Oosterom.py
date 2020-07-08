import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('bot is ready!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def hallo(ctx):
    await ctx.send('hallo! het is weer een mooie dag voor het proletariaat!')

@client.command(name='kcv', description = 'ik zal je vertellen wat kcv is')
async def kcv(ctx):
    await ctx.send('weet jij niet wat KCV is?!')
    time.sleep(2)
    await ctx.send('https://nl.wikipedia.org/wiki/Klassieke_culturele_vorming')



client.run('NzI5MDMyNDI4NTI5NjQ3NjQ2.XwDCxA.TYZzVhsuTtr2uLhHmM1AFcKssxU')
