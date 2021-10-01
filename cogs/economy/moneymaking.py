import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import aiosqlite
from random import randint

class MoneyMaking(commands.Cog):
    """MoneyMaking economy commands!"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('MoneyMaking commands are ready!')
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS users (userid INTEGER, bank INTEGER, wallet INTEGER);")
                await connection.commit()

    @commands.command()
    @commands.cooldown(1,15,commands.BucketType.user)
    async def beg(self, ctx):
        earnings = randint(
        1, 100
        )
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                    await connection.commit()
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:success:761297849475399710> {ctx.author.name} begs hard!", color = ctx.author.color)
                em.add_field(name = ":coin: Earnings", value = f"{earnings} :coin:", inline = False)
                em.set_thumbnail(url = ctx.author.avatar_url)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=em)

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def devwith(self, ctx, amount = None):
        if amount is None:
            await ctx.send("Type an amount!")
            return
        if not amount == 'all':
            amount = int(amount)
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0,))
                else:
                    if not amount == 'all':
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (rows[1] + amount, rows[0], ctx.author.id))
            await connection.commit()
        await ctx.send(f"Gave you {amount} :dollar:")

    @commands.command()
    @cooldown(1, 86400, BucketType.user)
    async def daily(self, ctx):
        earnings = 2000
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:success:761297849475399710> {ctx.author.name} begs hard!", color = ctx.author.color)
                em.add_field(name = ":dollar: Earnings", value = f"{earnings} :coin:", inline = False)
                em.add_field(name = ":tada: Free prize:", value = "Once a day you can claim a free price!")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                em.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1,30,commands.BucketType.user)
    async def serve(self, ctx):
        earnings = randint(
        1, 500
        )
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:success:761297849475399710> {ctx.author.name} serves their server!", color = ctx.author.color)
                em.add_field(name = ":coin: Earnings", value = f"{earnings} :coin:", inline = False)
                em.add_field(name = "Server:", value = f"{ctx.guild.name}")
                em.set_thumbnail(url = ctx.author.avatar_url)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=em)


    @commands.command()
    @cooldown(1, 604800, BucketType.user)
    async def weekly(self, ctx):
        earnings = 15000
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:success:761297849475399710> {ctx.author.name} begs hard!", color = ctx.author.color)
                em.add_field(name = ":dollar: Earnings", value = f"{earnings} :coin:", inline = False)
                em.add_field(name = ":tada: Free prize:", value = "Once a day you can claim a free price!")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                em.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=em)

    # Error handling with command handler!
    @serve.error
    async def serve_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Stop serving the server your in!")
            em.add_field(name = "Try again in:", value = "{:.2f} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Get back to studying!")
            seconds = round(error.retry_after)
            minutes = round(seconds / 60)
            hours = round(minutes / 60)
            em.add_field(name = "Try again in:", value = f"{hours} hours, {minutes} minutes and {seconds} seconds!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @weekly.error
    async def weekly_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Get back to studying! Weekly prizes are called weekly for a reason!")
            em.add_field(name = "Try again in:", value = "{:.2f}s".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @devwith.error
    async def devwith_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Your already too rich, Lord {ctx.author.mention}!")
            em.add_field(name = "Try again in:", value = "{:.2f} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Begging makes you look poor which you are {ctx.author.mention}!")
            em.add_field(name = "Try again in:", value = "{:.2f} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(MoneyMaking(client))
