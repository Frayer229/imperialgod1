import discord
from discord.ext import commands

class ReactionAdd(commands.Cog):
    def __init__(self, client):
        self.client=  client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("ReactionAdd event is ready!")
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        reaction = str(payload.emoji)

        return

def setup(client):
    client.add_cog(ReactionAdd(client))