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
    await client.change_presence(status = discord.Status.online, activity = discord.Game('retorica'))
    print('bot is ready!')

@client.event
async def on_member_join(member, ctx):
    print(f'{member} has joined the server!')

@client.event
async def on_member_remove(member, ctx):
    print(f'{member} has left the server')

@client.command()
async def hallo(ctx):
    await ctx.send('hallo! het is weer een mooie dag voor het proletariaat!')

@client.command(description = 'kcv')
async def kcv(ctx):
    await ctx.send('weet jij niet wat KCV is?!')
    time.sleep(2)
    await ctx.send('https://nl.wikipedia.org/wiki/Klassieke_culturele_vorming')

@client.command()
async def waarom(ctx):
    await ctx.send('daarom')

@client.command()
async def help(ctx):
    embed = discord.Embed(title = 'dit kan je met mij doen:', color = discord.Color.red())
    embed.add_field(name = '.help', value = 'zie de commands die ik heb', inline = False)
    embed.add_field(name = '.hallo', value = 'zeg hallo', inline = False)
    embed.add_field(name = '.kcv', value = 'laat mij vertellen over kcv', inline = False)
    embed.add_field(name = '.waarom', value = 'daarom')
    embed.add_field(name = '.ping', value = 'zie mijn ping', inline = False)
    embed.add_field(name = '.mysterie', value = 'wat zal dit command ons brengen?', inline = False)
    embed.add_field(name = '.praise', value = 'praise mij', inline = False)
    embed.add_field(name = '.meme', value = 'ik stuur je een meme uit r/memes', inline = False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    await ctx.send(f'mijn ping is {round(client.latency * 1000)} ms')

@client.command()
async def mysterie(ctx):
    await ctx.send('https://gph.is/2ehdc0q')

@client.command()
async def praise(ctx):
    await ctx.send('mijn dank is groot!')

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 40)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


client.run('NzI5MDMyNDI4NTI5NjQ3NjQ2.XwDCxA.TYZzVhsuTtr2uLhHmM1AFcKssxU')
