import dbl
import discord
from discord.ext import commands, tasks
import json
import aiosqlite

class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, client):
        self.client = client
        with open("./config.json", "r") as f:
            config = json.load(f)
        self.token = config["topToken"]
        self.dblpy = dbl.DBLClient(self.client, self.token)
        self.update_stats.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Top.gg stuff is ready!")

    @tasks.loop(minutes=30.0)
    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        try:
            await self.dblpy.post_guild_count()
        except Exception as e:
            print('Failed to post server count\n{}: {}'.format(type(e).__name__, e))

    @commands.Cog.listener()
    async def on_dbl_vote(self, data):
        # print(data)
        return
        
def setup(client):
    client.add_cog(TopGG(client))
