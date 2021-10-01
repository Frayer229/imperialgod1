import discord
from discord.ext import commands
import json
from .utils import * 

class PointEvents(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("PointEvents are Ready")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        with open("./data/points.json", "r") as f:
            points = json.load(f)
        
        if message.author.bot:
            return

        if str(message.guild.id) not in points:
            points[str(message.guild.id)] = {}
        
        if str(message.author.id) not in points[str(message.guild.id)]:
            points[str(message.guild.id)][str(message.author.id)] = 5
        
        else:
            points[str(message.guild.id)][str(message.author.id)] += 5

        with open("./data/points.json", "w") as f:
            json.dump(points, f)
    
    @commands.Cog.listener()
    async def on_command(self, ctx):
        with open("./data/points.json", "r") as f:
            points = json.load(f)

        if ctx.author.bot:
            return

        if str(ctx.guild.id) not in points:
            points[str(ctx.guild.id)] = {}

        if str(ctx.author.id) not in points[str(ctx.guild.id)]:
            points[str(ctx.guild.id)][str(ctx.author.id)] = 5
        else:
            points[str(ctx.guild.id)][str(ctx.author.id)] += 5

        with open("./data/points.json", "w") as f:
            json.dump(points, f)

def setup(client):
    client.add_cog(PointEvents(client))