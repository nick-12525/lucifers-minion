import discord
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import random
import time
import datetime
import asyncio
import psycopg2

bot = discord.Client()
bot = Bot(command_prefix="h~", pm_help = False, description="I only server Lucifer, not filthy peasants.")

class Administrator:

    @commands.command()
    async def prune(self, ctx, amount = None, user:discord.Member = None):
        """Prunes the last [x] amount of messages,
        if adding a user it will prune all their messages
        in the last [x] messages"""
        perms = ctx.message.author.permissions_in(ctx.channel)
        if not perms.manage_messages:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if amount == None:
                em = discord.Embed(title=":x: Error!", description = "Do {}help prune for help".format(bot.command_prefix), colour = discord.Colour.red())
                await ctx.send(embed = em)
            elif not amount.isdigit():
                em = discord.Embed(title = ":x: Error!", description = "Enter a number of messages to prune!", colour = discord.Colour.red())
                await ctx.send(embed = em)
            else:
                if user == None:
                    if int(amount)>=99:
                        amount = 98
                    amount = int(amount) + 1
                    await ctx.channel.purge(limit = amount)
                else:
                    to_delete = []
                    async for i in ctx.channel.history(limit=int(amount)):
                        if i.author == user:
                            await i.delete()
    @commands.command()
    async def kick(self, ctx, user:discord.Member = None):
        perms = ctx.message.author.guild_permissions
        if not perms.kick_members:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if user == None:
                em = discord.Embed(title = ":x: Error!", description = "Enter a member's name to kick!", colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                await user.kick()
                em = discord.Ember(title = "Kicked.", description="They don't even deserve to be in hell.", colour = discord.Colour.green())
                await ctx.send(embed = em)

    @commands.command()
    async def ban(self, ctx, user:discord.Member = None):
        perms = ctx.message.author.guild_permissions
        if not perms.ban_members:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if user == None:
                em = discord.Embed(title = ":x: Error!", description = "Enter a member's name to ban!", colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                await user.ban()
                em = discord.Ember(title = "Banned.", description="They are forever banished to TheLimbo.", colour = discord.Colour.green())
                await ctx.send(embed = em)

    @commands.command()
    async def mute(self, ctx, user:discord.Member = None, time = None):
        perms = ctx.message.author.permissions_in(ctx.channel)
        if not perms.manage_messages:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if user == None:
                em = discord.Embed(title = ":x: Error!", description = "Enter a member's name to mute!", colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                if time == None:
                    await ctx.channel.set_permissions(user, send_messages = False)
                    em = discord.Embed(title = "Muted", description = "Finally peace and quiet, we don't get much of that in hell.", colour = discord.Colour.green())
                    await ctx.send(embed = em)
                else:
                    if not time.isdigit():
                        em = discord.Embed(title = ":x: Error!", description = "Enter the time in seconds", colour = discord.Colour.red())
                        msg = await ctx.send(embed = em)
                        await asyncio.sleep(3)
                        await msg.delete()
                    else:
                        time = int(time)
                        await ctx.channel.set_permissions(user, send_messages = False)
                        em = discord.Embed(title = "Muted for {} seconds".format(time), description = "Finally peace and quiet, we don't get much of that in hell.", colour = discord.Colour.green())
                        await ctx.send(embed = em)
                        await asyncio.sleep(time)
                        await ctx.channel.set_permissions(user, send_messages = True)

    @commands.command()
    async def unmute(self, ctx, user:discord.Member = None):
        perms = ctx.message.author.permissions_in(ctx.channel)
        if not perms.manage_messages:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if user == None:
                em = discord.Embed(title = ":x: Error!", description = "Enter a member's name to unmute!", colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                await ctx.channel.set_permissions(user, send_messages = True)
                em = discord.Embed(title = "Unmuted {}".format(user.name), description="Oh great they can speak again.", colour = discord.Colour.green())
                await ctx.send(embed = em)

class CustomReactions:
    @commands.group(aliases = ['cr', 'custreact'])
    async def customreact(self, ctx):
        if ctx.invoked_subcommand is None:
            em = discord.Embed(title = ":x: Error", description = "Use {}help cr for help".format(bot.command_prefix), colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()

    @customreact.command()
    async def add(self, ctx, message = None, *, reaction = None):
        """Put the message in " " when adding."""
        perms = ctx.message.author.permissions_in(ctx.channel)
        if not perms.manage_messages:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if message == None:
                em = discord.Embed(title = ":x: Error", description = "Use `{}help cr add` for help".format(bot.command_prefix), colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                if reaction == None:
                    em = discord.Embed(title = ":x: Error", description = "Use `{}help cr add` for help".format(bot.command_prefix), colour = discord.Colour.red())
                    msg = await ctx.send(embed = em)
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    serverid = ctx.guild.id
                    conn = psycopg2.connect(database="da5rfaqi7o9cg7", user="coptashatlyxvu", password="df29244125a967ef825b3c4c5bfecacaf0cf15c91da9d6da845d83794ffdb113", host="ec2-79-125-110-209.eu-west-1.compute.amazonaws.com", port="5432")
                    cur = conn.cursor()
                    cur.execute("""INSERT INTO customreacts(server, message, reaction) VALUES(%s, %s, %s) RETURNING id;""",
                                (serverid, str(message), str(reaction)))
                    reactid = cur.fetchone()[0]
                    conn.commit()
                    cur.close()
                    conn.close()
                    em = discord.Embed(title = "Added", colour = discord.Colour.green())
                    em.add_field(name="Id", value=str(reactid), inline=True)
                    em.add_field(name="Message", value=str(message), inline=True)
                    em.add_field(name="Reaction", value=str(reaction), inline=True)
                    await ctx.send(embed = em)

    @customreact.command(aliases = ['del', 'd'])
    async def delete(self, ctx, reactid = None):
        perms = ctx.message.author.permissions_in(ctx.channel)
        if not perms.manage_messages:
            em = discord.Embed(title = ":x: Error!", description = "You have insufficient permissions!", colour = discord.Colour.red())
            msg = await ctx.send(embed = em)
            await asyncio.sleep(3)
            await msg.delete()
        else:
            if reactid == None:
                em = discord.Embed(title = ":x: Error", description = "Enter a reaction ID to delete.".format(bot.command_prefix), colour = discord.Colour.red())
                msg = await ctx.send(embed = em)
                await asyncio.sleep(3)
                await msg.delete()
            else:
                conn = psycopg2.connect(database="da5rfaqi7o9cg7", user="coptashatlyxvu", password="df29244125a967ef825b3c4c5bfecacaf0cf15c91da9d6da845d83794ffdb113", host="ec2-79-125-110-209.eu-west-1.compute.amazonaws.com", port="5432")
                cur = conn.cursor()
                cur.execute("""SELECT serverid, message, reaction FROM customreacts WHERE id = %s;""",
                            ([reactid]))
                deleted = cur.fetchone()
                if deleted[0] != ctx.guild.id:
                    em = discord.Embed(title = ":x: Error!", description = "That isn't a valid ID!", colour = discord.Colour.red())
                    msg = await ctx.send(embed = em)
                    await asyncio.sleep(3)
                    await msg.delete()
                else:
                    cur.execute("""DELETE FROM customreacts WHERE id = %s;""",
                            ([reactid]))
                    rowdel = cur.rowcount
                    conn.commit()
                    cur.close()
                    conn.close()
                    if int(rowdel) == 1:
                        em = discord.Embed(title="Deleted:", colour = discord.Colour.green())
                        em.add_field(name="Id", value=str(reactid), inline = True)
                        em.add_field(name="Message", value=str(deleted[1]), inline=True)
                        em.add_field(name="Reaction", value=str(deleted[2]), inline=True)
                        await ctx.send(embed = em)
                    else:
                        em = discord.Embed(title=":x:Error", description="No reaction with that ID could be found.", colour = discord.Colour.red())
                        await ctx.send(embed = em)

    
class Miscellanious:
    async def invite(ctx):
        """Invite the bot!"""
        await ctx.send("https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(bot.user.id))


@bot.event
async def on_ready():
    print("Ready af!")

@bot.event
async def on_message(message):
    m = str(message.content)
    conn = psycopg2.connect(database="da5rfaqi7o9cg7", user="coptashatlyxvu", password="df29244125a967ef825b3c4c5bfecacaf0cf15c91da9d6da845d83794ffdb113", host="ec2-79-125-110-209.eu-west-1.compute.amazonaws.com", port="5432")
    cur = conn.cursor()
    cur.execute("""SELECT message, reaction FROM customreacts WHERE server = %s;""",
            ([str(message.guild.id)]))
    mr = cur.fetchone()
    found = []
    while mr is not None:
        if mr[0] == m:
            found.append(mr)
        mr = cur.fetchone()
    cur.close()
    conn.close()
    if found != []:
        ms = random.choice(found)
        reaction = ms[1]
        await message.channel.send(reaction)

    await bot.process_commands(message)

bot.add_cog(Administrator())
bot.add_cog(CustomReactions())
bot.add_cog(Miscellanious())
bot.run("UwMjMxMTU3MzIyMTUzOTk0.DewN_w.v3c_1c0gNCfPkYygoNS1-0VEczE")
