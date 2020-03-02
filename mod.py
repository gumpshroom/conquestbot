import discord
import random
from discord.ext import commands




@client.command()
async def kick(ctx, member : discord.Member, *, reason=nothing):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked because of {reason}')


@client.command()
async def ban(ctx, member : discord.Member,     *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been baned because of {reason}')


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return








#purging
@client.command()
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
