import discord
import json
from discord.ext import commands

class Points(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Points are ready!")
    
    @commands.command()
    async def points(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        with open("./data/points.json", "r") as f:
            points = json.load(f)
        
        if str(ctx.guild.id) not in points:
            points[str(ctx.guild.id)] = {}
        
            if str(member.id) not in points[str(ctx.guild.id)]:
                points[str(ctx.guild.id)][str(member.id)] = 0  
                member_points = points[str(ctx.guild.id)][str(member.id)]        
        else:
            member_points = points[str(ctx.guild.id)][str(member.id)]

        em = discord.Embed(title = f"<:success:761297849475399710> {member.name}'s Points", color = member.color, description = f"This embed shows how many points {member.mention} has!")
        em.set_thumbnail(url = member.avatar_url)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.add_field(name = "Points:", value = f"`{member_points}`")
        if member_points > 5000:
            em.set_footer(text = f"Oi {member.name} rich as hell boi", icon_url = member.avatar_url)
        await ctx.send(embed = em)
    
        with open("./data/points.json", "w") as f:
            json.dump(points, f)
    
    @commands.command()
    async def pointsper(self, ctx):
        em = discord.Embed(title = "Pointsper", color = ctx.author.color, description = "Every time you take an action I will hand you out points!\n```diff\n+ 1 Message = 5 points\n- 1 Command = 5 points\n```")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "Grind for points and get a role 😋", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @commands.command()
    async def givepoints(self, ctx, member: discord.Member = None, points_ = None, *, reason: str = None):
        if member is None:
            await ctx.send("Give me a member to give points to!")
            return
        elif points_ is None:
            await ctx.send("Give some valid points!")
            return 
        
        try:
            real_points = int(points_)
        except:
            await ctx.send('Please provide an integer as the points!')

        if real_points < 0 or real_points == 0:
            await ctx.send('The points should be a positive integer!')
            return
    
        with open("./data/points.json", "r") as f:
            points = json.load(f)
        
        # define the author's points
        if str(ctx.guild.id) not in points:
            points[str(ctx.guild.id)] = {}
            points[str(ctx.guild.id)][str(ctx.author.id)] = 0
            points[str(ctx.guild.id)][str(member.id)] = 0
            author_points = 0
        else:
            if str(ctx.author.id) not in points[str(ctx.guild.id)]:
                points[str(ctx.guild.id)][str(ctx.author.id)] = 0
                author_points = 0
            elif str(member.id) not in points[str(ctx.guild.id)]:
                points[str(ctx.guild.id)][str(member.id)] = 0
            author_points = points[str(ctx.guild.id)][str(ctx.author.id)]
        
        if real_points > author_points:
            await ctx.send('You don\'t even have those many points idiot!')
            return

        points[str(ctx.guild.id)][str(ctx.author.id)] -= real_points
        points[str(ctx.guild.id)][str(member.id)] += real_points

        embed = discord.Embed(title=  "<:success:761297849475399710> Points Given", color = ctx.author.color, description = f"<:success:761297849475399710> We gave {member.mention} `{real_points}` points, graciously given by: {ctx.author.mention}")
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.add_field(name = 'From:', value = ctx.author.mention)
        embed.add_field(name = 'To:',value =  member.mention)
        embed.add_field(name = "Amount:", value = f'`{real_points}`')
        embed.add_field(name = 'Reason', value = f'`{reason}`')
        embed.set_footer(text = "Contact the empire at https://theimperialgod.ml", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

        with open('./data/points.json', 'w') as f:
            json.dump(points, f)

    @commands.command(aliases=["pointsinfo","helppoints","infopoints"])
    async def pointshelp(self,ctx):
        em=discord.Embed(title="Points system",description="Help about points system",color=ctx.author.color,url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        em.add_field(name="Points",value="Points are imaginary points that are accumulated whenever you chat or use my commands.")
        em.add_field(name="Leaderboards",value="The leaderboards is the list of members with the highest points in the server.")
        em.add_field(name="Crown role",value="The CROWN is a special role given to the person who is top in the leaderboards, the role member will be hoisted!")
        em.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
        em.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Points(client))