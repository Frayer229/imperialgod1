import discord
from discord.ext import commands
import json

class Patching(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.ownerIds = [575706831192719370, 437163344525393920, 717724055217635398]
        self.patched = None
        with open('./config.json', 'r') as f:
            config = json.load(f)
        self.patchId = config['IDs']['patchId']
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Patching is ready!')

    @commands.group(invoke_without_command = True)
    async def patch(self, ctx):
        if ctx.author.id not in self.ownerIds:
            return await ctx.send('Restricted access!')
        
        self.patched = discord.Embed(title = 'New Patch', color = discord.Color.random())
        self.patched.set_thumbnail(url = ctx.author.avatar_url)
        self.msg = "```diff\n"
        await ctx.send('Patch created!')
    
    @patch.command()
    async def add(self,ctx, *, message):
        self.msg += f"{message}\n"
        await ctx.send('Added the message!')
    
    @patch.command()
    async def post(self, ctx):
        self.msg += '\n```'
        self.patched.description = self.msg
        channel = self.client.get_channel(self.patchId)
        await channel.send(embed = self.patched)
        await ctx.send(f"Posted the patch in {channel.mention}")


def setup(client):
    client.add_cog(Patching(client))