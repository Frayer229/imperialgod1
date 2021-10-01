import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import praw
import random
from json import load

class Animals(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./config.json", "r") as f:
            config = load(f)

        self.reddit = praw.Reddit(
            client_id = config["reddit"]["clientId"],
            client_secret = config["reddit"]["clientSecret"],
            username = config["reddit"]["username"],
            password = config["reddit"]["password"],
            user_agent = config["reddit"]["userAgent"]
        )

    @commands.Cog.listener()
    async def on_ready(self):
        print("Animal module loaded!")

    @commands.command()
    async def dog(self, ctx):
        subreddit = self.reddit.subreddit("dog")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def cat(self, ctx):
        subreddit = self.reddit.subreddit("cat")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)   

    @commands.command()
    async def duck(self, ctx):
        subreddit = self.reddit.subreddit("duck")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def fox(self, ctx):
        subreddit = self.reddit.subreddit("fox")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def panda(self, ctx):
        subreddit = self.reddit.subreddit("panda")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def koala(self, ctx):
        subreddit = self.reddit.subreddit("koala")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def tiger(self, ctx):
        subreddit = self.reddit.subreddit("tiger")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def lion(self, ctx):
        subreddit = self.reddit.subreddit("lion")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["snek"])
    async def snake(self, ctx):
        subreddit = self.reddit.subreddit("snake")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def owl(self, ctx):
        subreddit = self.reddit.subreddit("owl")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["pandared", "rpanda", "pandr"])
    async def redpanda(self, ctx):
        subreddit = self.reddit.subreddit("redpanda")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["mem", "goodmem", "meme"])
    @cooldown(1, 10, BucketType.user)
    async def _meme(self, ctx):
        subreddit = self.reddit.subreddit("meme")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @_meme.error
    async def _meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Meme Error", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Stop seeing memes too much, or you will become a meme!")
            em.add_field(name = "Try Again In:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Animals(client))
