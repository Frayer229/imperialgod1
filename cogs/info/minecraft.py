import discord
from discord.ext import commands
import aiomojang

class Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Minecraft cog is ready!")

    """
    I stole this from the examples cuz why not lmao
    Huge credit to capslock for doing this. 
    """    
    @commands.command(aliases=["minecraftstats", "statsminecraft", "mcstats"])  # Get information on a player.
    async def mojang(self, ctx, player: str):
        profile = aiomojang.Player(player)
        try:
            embed = discord.Embed(title=f"<:success:761297849475399710> Information on {player}: ", color=ctx.author.color)
            embed.add_field(name="Player's name: ", value=player)  # Because doing profile.name will raise an error.
            embed.add_field(name="Player's uuid: ", value=await profile.uuid, inline=False)
            embed.set_image(url = await profile.get_skin())
            embed.set_author(name = player, icon_url = await profile.get_skin())
            embed.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
            await ctx.send(embed=embed)
        except aiomojang.exceptions.ApiException:
            return await ctx.send(f"No user with the name {player} was found.")

    @commands.command(aliases=["mchistory"])  # Name history command
    async def history(self, ctx, player: str):
        profile = aiomojang.Player(player)
        embed = discord.Embed(title=f"{player}'s name history: ", color=discord.Colour.blue())
        i = 1
        for x in await profile.get_history():
            embed.add_field(name = f"Name #{i}: ", value = x['name'])  # Iterate through the names.
            i = i + 1
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Minecraft(client))