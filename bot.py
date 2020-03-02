import discord
import os
import random
from discord.ext import commands, tasks
import fun
import mod

client = commands.Bot(command_prefix = '?')

@client.command()
async def on_ready():
    print('Bot is ready.'.format(client))

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('NjgyMDEwMjc2NTk3NDY1MTcy.Xlbo8Q.Ri640-2wwMtK9n8P8pbLny8BZtk')

execfile('fun.py')
execfile('mod.py')
