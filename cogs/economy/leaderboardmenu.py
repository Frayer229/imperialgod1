from discord.ext import menus
import discord

class LeaderboardMenu(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=5)

    async def format_page(self, menu, entries):
        embed = discord.Embed(title='🏆 Top 10 users 🏆',description='Sorted by the total of wallet and bank balance combined')
        place = 0

        for row in entries:
            place += 1
            user = row[0]
            embed.add_field(name=f'{user}',value=f"**Bank:** {row[1]}\n**Wallet:** {row[2]}\n**Total:** {row[1] + row[2]}",inline=False)
        return embed