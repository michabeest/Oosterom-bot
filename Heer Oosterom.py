import discord
import time
import praw
import random
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

client.remove_command('help')

reddit = praw.Reddit(client_id = 'DkVy9B-_J5k5Hg', client_secret = 'e1iyuhHdcEQkATBgD-PdcOz3_lI', user_agent = 'micha')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game('Retorica'))
    print('bot is ready!')

@client.event
async def on_member_join(member, ctx):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member, ctx):
    print(f'{member} has left the server')

@client.command()
async def hallo(ctx):
    await ctx.send('Hallo! Het is weer een mooie dag voor het proletariaat!')

@client.command(description = 'kcv')
async def kcv(ctx):
    await ctx.send('Weet jij niet wat KCV is?!')
    time.sleep(2)
    await ctx.send('https://nl.wikipedia.org/wiki/Klassieke_culturele_vorming')

@client.command()
async def waarom(ctx):
    await ctx.send('Daarom')

@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'Dit kan je met mij doen:', color = discord.Color.red())
    embed.add_field(name = '.help', value = 'Zie de commands die ik heb', inline = False)
    embed.add_field(name = '.hallo', value = 'Zeg hallo', inline = False)
    embed.add_field(name = '.kcv', value = 'Laat mij vertellen over kcv', inline = False)
    embed.add_field(name = '.retorica', value = 'Laat mij vertellen over retorica', inline = False)
    embed.add_field(name = '.waarom', value = 'Daarom')
    embed.add_field(name = '.ping', value = 'Zie mijn ping', inline = False)
    embed.add_field(name = '.mysterie', value = 'Wat zal dit command ons brengen?', inline = False)
    embed.add_field(name = '.praise', value = 'Praise mij', inline = False)
    embed.add_field(name = '.meme', value = 'Ik stuur je een meme uit r/memes', inline = False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'Mijn ping is {round(client.latency * 1000)} ms')

@client.command()
async def praise(ctx):
    await ctx.send('Mijn dank is groot!')

@client.command()
async def mysterie(ctx):
    await ctx.send('https://giphy.com/gifs/lgcUUCXgC8mEo')

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 40)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@client.command()
async def retorica(ctx):
    await ctx.send('Retorica (van het Oudgriekse woord ῥήτωρ, rhêtôr, spreker, leraar; oude Nederlandse spelling rhetorica met rh-), letterlijk redenaarskunst, of welsprekendheid, is de kunst van het spreken in het openbaar. Retorica, dat uit de klassieke oudheid is voortgekomen, is daarmee de oudste westerse teksttheorie. De term staat voor welsprekendheid, maar in uitgebreide zin slaat het op effectief spreken en schrijven en de kunst van het overtuigen. Men gebruikt het begrip dus zowel voor de theorie – de leer van overtuigend spreken en schrijven of retorica – als voor de praktijk ervan. ')

client.run('NzI5MDMyNDI4NTI5NjQ3NjQ2.XwDCxA.TYZzVhsuTtr2uLhHmM1AFcKssxU')
