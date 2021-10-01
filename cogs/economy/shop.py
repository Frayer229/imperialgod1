"""
HUGE THANKS TO BotDotBot's code and BotDotCom for writing some of the logic.
Be sure to check that file here: https://github.com/BobDotCom/BobDotBot/blob/main/cogs/economy.py
Follow him: https://github.com/BotDotCom
Make sure you do that, cause its been taken inspiration from by using his system!

not 100% but like 60%
"""

import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import aiosqlite
import asyncio

class Shop(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Shop commands are ready")
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS shop (id INTEGER, name TEXT, price INTEGER, available BOOL)")
                await connection.commit()

    @commands.group(invoke_without_command = True)
    @cooldown(1, 20, BucketType.user)
    async def shop(self, ctx):
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM shop WHERE available = ?", (True,))
                items = await cursor.fetchall()

                em = discord.Embed(title = "Shop", color = ctx.author.color)
                for item in items:
                    em.add_field(name = f"{item[1]}", value = f"Cost: {item[2]}\nID: {item[3]}")
                await ctx.channel.send(embed = em)
                await connection.commit()

    @shop.error
    async def shop_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"<:fail:761292267360485378> Slow it down C'mon", color=ctx.author.color)
            em.add_field(name=f"Reason:", value="You can always see the shop idiot!")
            em.add_field(name="Try again in:", value="{:.2f} seconds".format(error.retry_after))
            em.set_thumbnail(url=ctx.author.avatar_url)
            await ctx.send(embed=em)

    @shop.command()
    @commands.is_owner()
    async def add(self, ctx, name, price : int):
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                def check(m):
                    return m.author == ctx.author and m.channel == ctx.channel

                try:
                    await ctx.send("Type the availibility for this item! (True or False)")
                    msg = await self.client.wait_for('message', timeout=15.0, check=check)
                except asyncio.TimeoutError:
                    await ctx.send('You didn\'t answer in time, please be quicker next time!')
                    return
                else:
                    if msg.content.lower() == "true":
                        await cursor.execute("INSERT INTO shop (name, price, available) VALUES (?, ?, ?)", (name, price, True,))
                    elif msg.content.lower() == "false":
                        await cursor.execute("INSERT INTO shop (name, price, available) VALUES (?, ?, ?)", (name, price, False,))
                    await cursor.execute('SELECT id FROM shop')
                    rows = await cursor.fetchall()
                    number = rows[-1][0]
                    await cursor.execute(f'ALTER TABLE users ADD COLUMN item{number} INTEGER;')
                    await connection.commit()

        await ctx.send(f"{ctx.author.mention}, item was created!\nName: {name} | Price {price} | ID = {number}")

    @shop.command()
    @commands.is_owner()
    async def remove(self, ctx, item_id):
        item_id = int(item_id)
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM shop WHERE id = ? AND available = ?", (item_id, True,))
                rows = await cursor.fetchone()
                if rows:
                    await ctx.send(f"Successfully removed item `{item_id}` from the shop")
                else:
                    await ctx.send("That item doesnt exist")
                    return
                await cursor.execute("UPDATE shop SET available = ? WHERE id = ?", (False, item_id,))
                await connection.commit()

    @shop.command()
    @commands.is_owner()
    async def enable(self, ctx, item_id):
        item_id = int(item_id)
        async with aiosqlite.connect("economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM shop WHERE id = ? AND available = ?", (item_id, False,))
                rows = await cursor.fetchone()
                if rows:
                    await ctx.send(f"Successfully enabled item `{item_id}` in the shop")
                else:
                    await ctx.send("That item doesnt exist or is enabled")
                await cursor.execute("UPDATE shop SET available = ? WHERE id = ?", (True, item_id,))
                await connection.commit()

    @shop.command()
    @commands.is_owner()
    async def edit(self, ctx, item_id, price):
        item_id = int(item_id)
        price = int(price)
        async with aiosqlite.connect("economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("UPDATE shop SET price = ? WHERE id = ?", (price, item_id,))
                await connection.commit()
        await ctx.send(f"Successfully changed price of item `{item_id}` to `{price}`")

def setup(client):
    client.add_cog(Shop(client))