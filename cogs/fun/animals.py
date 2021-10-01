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
    
    async def get_random_post(self, member, subreddit_ = None, limit= 100):
        try:
            if subreddit_ is not None:
                subreddit = self.reddit.subreddit(subreddit_)

            top = subreddit.top(limit = limit)
            all_subs = []

            for sub in top:
                all_subs.append(sub)
            
            sub = random.choice(all_subs)
            embed = discord.Embed(title = f"{sub.title}", color = member.color)
            embed.set_image(url = sub.url)
            embed.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            return embed
        except:
            em = discord.Embed(title = "<:fail:761292267360485378> API Error", color = member.color, description = "My API was unable to send you an image! We are sorry for the inconvinience. If this becomes a serious issue contact NightZan999!")
            em.add_field(name = "Reason:", value = "idunno man but praw sucks")
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            return em

    @commands.Cog.listener()
    async def on_ready(self):
        print("Animal module loaded!")

    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def dog(self, ctx):
        em = await self.get_random_post(ctx.author, "dog")
        await ctx.send(embed = em)
    
    @dog.error
    async def dog_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def cat(self, ctx):
        em = await self.get_random_post(ctx.author, "cat")
        await ctx.send(embed = em)
    
    @cat.error
    async def cat_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def duck(self, ctx):
        em = await self.get_random_post(ctx.author, "duck")
        await ctx.send(embed = em)
    
    @duck.error
    async def duck_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        
    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def fox(self, ctx):
        em = await self.get_random_post(ctx.author, "fox")
        await ctx.send(embed = em)

    @fox.error
    async def fox_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def panda(self, ctx):
        em = await self.get_random_post(ctx.author, "panda", 10)
        await ctx.send(embed = em)

    @panda.error
    async def panda_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def koala(self, ctx):
        em = await self.get_random_post(ctx.author, "koala", 10)
        await ctx.send(embed = em)

    @koala.error
    async def koala_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)


    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def tiger(self, ctx):
        em = await self.get_random_post(ctx.author, "fox")
        await ctx.send(embed = em)

    @tiger.error
    async def tiger_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases=["lian"])
    @cooldown(1, 5, BucketType.user)
    async def lion(self, ctx):
        em = await self.get_random_post(ctx.author, "lion", 10)
        await ctx.send(embed = em)

    @lion.error
    async def lion_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def snake(self, ctx):
        em = await self.get_random_post(ctx.author, "snake", 10)
        await ctx.send(embed = em)

    @snake.error
    async def snake_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def owl(self, ctx):
        em = await self.get_random_post(ctx.author, "owl", 20)
        await ctx.send(embed = em)

    @owl.error
    async def owl_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def redpanda(self, ctx):
        em = await self.get_random_post(ctx.author, "snake", 10)
        await ctx.send(embed = em)

    @redpanda.error
    async def redpanda_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=  "<:fail:761292267360485378> Command On Cooldown", color = member.color)
            em.add_field(name = "Reason:", value = "Command On Cooldown!")
            em.add_field(name = "Try Again in:", value = "{.:2f}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
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
        embed.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @_meme.error
    async def _meme_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Meme Error", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Stop seeing memes too much, or you will become a meme!")
            em.add_field(name = "Try Again In:", value = "{:.2}s".format(error.retry_after))
            em.set_footer(text = "To support me invite me!", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
def setup(client):
    client.add_cog(Animals(client))
