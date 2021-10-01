import json
from discord.ext import commands
import discord
import dbl
import aiosqlite
from .config import Config

class Exclusive(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./config.json", "r") as f:
            config = json.load(f)
        self.token = config["topToken"]
        self.dblpy = dbl.DBLClient(self.client, self.token)
    
    @commands.group(invoke_without_command = True, aliases=["cr", "rewards", "claimreward", "reward"])
    async def claimrewards(self, ctx):
        em = discord.Embed(title=  "<:zancool:819065864153595945> Be Cool and claim rewards!", color = ctx.author.color)
        em.add_field(name = "Possible Subcommands:", value = '`vote`, `friends`')
        em.add_field(name = "Explanation:", value = "Vote can be used to collect voting rewards, and friends gives you rewards if you are a friend of the owner and you have voted!")
        await ctx.send(embed = em)

    @claimrewards.command()
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def vote(self, ctx):
        vote = await self.dblpy.get_user_vote(ctx.author.id)
        if not vote:
            ctx.command.reset_cooldown(ctx)
            await ctx.send("Mate, you need to vote for me to get access to this 15 grand\nVote Here: https://top.gg/bot/768695035092271124")
            return
        
        earnings = 15000
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                    await connection.commit()
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:zancool:819065864153595945> {ctx.author.name} claims their reward!", color = ctx.author.color)
                em.add_field(name = ":coin: Amount", value = f"{earnings} :coin:", inline = False)
                em.add_field(name = "Rewards", value = "Claim this in 1 hour, till then keep voting and giving me reviews :DD")
                em.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=em)


    @claimrewards.command()
    @commands.cooldown(1, 10800, commands.BucketType.user)
    async def friends(self, ctx):
        vote = await self.dblpy.get_user_vote(ctx.author.id)
        if not vote:
            ctx.command.reset_cooldown(ctx)
            await ctx.send("Mate, you need to vote for me to get access to this 15 grand\nVote Here: https://top.gg/bot/768695035092271124")
            return

        if int(ctx.author.id) not in Config.friends:
            ctx.command.reset_cooldown(ctx)
            await ctx.send("You are not my friend, back off!")
            return
        
        earnings = 50000
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                    await connection.commit()
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:zancool:819065864153595945> Well, you are a friend of mine!", color = ctx.author.color)
                em.add_field(name = ":coin: Amount", value = f"{earnings} :coin:", inline = False)
                em.add_field(name = "Rewards", value = "Claim this in 1 hour, till then keep voting and giving me reviews :DD")
                em.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=em)

    @friends.error
    async def friends_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Stop claiming rewards instead study!")
            em.add_field(name = "Try again in:", value = "**{}** minutes".format(int(error.retry_after / 60)))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @vote.error
    async def vote_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Stop claiming rewards instead study!")
            em.add_field(name = "Try again in:", value = "**{}** minutes".format(int(error.retry_after / 60)))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Exclusive(client))
    