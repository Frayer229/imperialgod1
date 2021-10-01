import discord
from discord.ext import menus

class ExampleMenu(menus.ListPageSource):
    def __init__(self, data):
        self.data = data
        super.__init__(data, items_per_page = 5)
    
    async def format_page():
        em = discord.Embed(title = "Example Users")
        async with aiosqlite.connect("database.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM users;")
                rows = await cursor.fetchall()
                # loop through the rows
                for row in rows:
                    em.add_field(name = f"Wallet | Bank", value = f"{rows[0]} | {rows[1]}")

        return em

class ReactionMenu(ExampleMenu):
    def __init__(self, msg):
        self.msg = msg
    
    async def add_reactions():
        await self.msg.add_reaction("⏮️")
        await self.msg.add_reaction("⏪")
        await self.msg.add_reaction('🔐')
        await self.msg.add_reaction('⏩')
        await self.msg.add_reaction('⏭️')

    async def get_latest_react():
        pass