import discord
from discord.ext import commands

class ReactionRemove(commands.Cog):
    def __init__(self, client):
        self.client=  client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ReactionRemove event is ready!")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        pass

def setup(client):
    client.add_cog(ReactionRemove(client))