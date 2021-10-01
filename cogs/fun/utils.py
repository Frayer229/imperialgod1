import discord
from discord.ext import commands
from random import choice
import traceback
import random

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client    
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Server Utilties are ready to be used!")

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def coinflip(self, ctx):
        em = discord.Embed(title = "Coinflip", color = ctx.author.color)
        choices = ["Heads", "Tails"]
        em.add_field(name = "Roll:", value = f"`{choice(choices)}` :coin:")
        return await ctx.send(embed = em)

    @commands.command(aliases=["rn"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def random_number(self, ctx, range1, range2):
        try:
            range1 = int(range1)
            range2 = int(range2)
        except:
            return await ctx.send("The ranges should be integers! You have not typed integers!")
        
        else:
            if (range1 > range2):
                return ctx.channel.send("the first range must be smaller than the second, idiot!")
            elif range1 == range2:
                return ctx.channel.send("the first range must be smaller than the second, not the same idiot!")
            num = randint(range1, range2)
            await ctx.send("Random number is `{}`".format(num))        

    @commands.command()
    async def code(self, ctx, *, msg = None):
        if msg == None:
            return await ctx.send("You have to provide a valid message:\n `imp code hello there`")

        await ctx.send("```" + msg.replace("`", "") +("```"))
    
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def thank(self, ctx, member: discord.Member = None, *, reason = None):
        if member is None:
            return await ctx.send("Provide a valid member!")
        elif reason is None:
            return await ctx.send("Provide a valid reason after the member!")
        elif member == ctx.author:
            return await ctx.send('You cannot thank yourself!')
        
        thanks = discord.Embed(title = f"{ctx.author.name} thanks someone!", color = ctx.author.color)
        thanks.add_field(name = "Member:", value = f"{member.mention}")
        thanks.add_field(name = 'Reason:', value = f"{reason}")
        thanks.add_field(name = 'User:', value = f"{ctx.author.mention}")
        return await ctx.send(embed = thanks)

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def reverse(self, ctx,*,msg = None):
        if msg is None:
            return await ctx.send("Provide a message to reverse!")
        try:
            msg = list(msg)
            msg.reverse()
            print(msg)
            send = ''.join(msg)
            await ctx.send(send)
        except Exception:
            traceback.print_exc()
        
    @commands.command(aliases=["8ball", "fate", "9ball"])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def eightball(self, ctx, *, question):
        responses = [
            'That is certain',
            'Of course',
            'My sources say yes',
            'Try again',
            'Bad internet try again',
            'No',
            'Never',
            'Always true',
            'My sources say no!'
        ]
        await ctx.send(f'Question: {question}\nAnswer: {choice(responses)}')

    @commands.command()
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def poll(self, ctx, *, message):
        embed = discord.Embed(title = f"{ctx.author.name}'s Poll", color = ctx.author.color, description = f"Poll by {ctx.author.name}")
        embed.add_field(name = f"{message}", value = "Share your thoughts about this topic")

        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("<:success:761297849475399710>")
        await my_msg.add_reaction("<:fail:761292267360485378>")

    @commands.command(aliases = ['str', 'show_tp', 's_toprole'])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        if member is None:
            member = ctx.author
        await ctx.send(f'The top role for {member.name} is {member.top_role.name}')
        
    @commands.command(aliases = ['generator','password','passwordgenerator', 'passwordgen'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def _pass(self, ctx,amt : int = 8):
        if amt <= 0:
            return await ctx.send("Amount of characters must be positive!")
        try:
            password = ""
            all_char = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z','!','@',
            '#','$','%','^','&','*','(',')','-','_','+','=','{',",",'}',']',
            '[',';',':','<','>','?','/','1','2','3','4','5','6','7','8','9','0'
            ,'`','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
            ,'Q','R','S','T','U','V','W','X','Y','Z'] #all char
            for x in range(amt):
                newpass = random.choice(all_char)
                password += newpass

            fnpss = ''.join(password)
            await ctx.send(f'{ctx.author} attempting to send you the genereated password in dms.')
            await ctx.author.send(f'Password Generated: {fnpss}')
        except Exception as e:
            print(e)
    
    @commands.command(aliases = ["av"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            em = discord.Embed(description=f"[**{ctx.author.name}'s Avatar**]({ctx.author.avatar_url})", colour=ctx.author.color, timestamp =ctx.message.created_at)
            em.set_image(url= ctx.author.avatar_url)
            em.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author}")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=em)

            return

        else:
            em = discord.Embed(description=f"[**{member.name}'s Avatar**]({member.avatar_url})", colour = member.color, timestamp =ctx.message.created_at)
            em.set_image(url=member.avatar_url)
            em.set_footer(icon_url = member.avatar_url, text = f"Requested by {ctx.author}")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed=em)

            return
    

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def respect(self, ctx, *, reason = None):
        em = discord.Embed(title = f'{ctx.author.name} gives respect!', color = ctx.author.color)
        em.add_field(name = "Reason:", value = f"{choice(['🤎','🧡', '💚', '💙', '💜'])} {reason}")
        em.add_field(name = "Respected Command Author:", value = f"{ctx.author.name}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def beer(self, ctx, member : discord.Member = None, *, reason = None):
        if member is None:
            return await ctx.send(f"{ctx.author.name} party!! 🎉🍺")
        
        if member == self.client.user:
            return await ctx.send("drinks beer with you* 🍻")
        
        em = discord.Embed(title = "Beer Invitation 🍺", color = ctx.author.color)
        em.add_field(name = "Member:", value = f"{member.mention}")
        em.add_field(name=  "Inviter:", value = f"{ctx.author.mention}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        if reason is not None:
            em.add_field(name = "Reason:", value = f"`{reason}`")
        msg = await ctx.send(content = f"{member.mention} to accept {ctx.author.mention}'s beer invite. React with beer to this embed!", embed = em)
        await msg.add_reaction("🍺")

        def check(reaction, user):
            return user == member and str(reaction.emoji) == "🍺"

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=15.0, check=check)

        except asyncio.TimeoutError:
            msg=(f"{member.mention} didn't accept the beer in time!")
            await ctx.channel.send(msg)

        else:
            successEmbed = discord.Embed(title = "<:success:761297849475399710> Beer Successful!", color = ctx.author.color, description = f"{member.name} and {ctx.author.name} are enjoing a lovely beer 🍻!").add_field(name = "Member:", value = f"{member.mention}").add_field(name=  "Inviter:", value = f"{ctx.author.mention}")
            return await msg.edit(embed = successEmbed, content = f"{member.mention} accepted the beer!")

    @commands.command()
    async def beerparty(self, ctx):
        em = discord.Embed(title = "Beer Invitation 🍻", color = ctx.author.color)
        em.add_field(name = "Time Left to join:", value = f"`10s`")
        em.add_field(name=  "Inviter:", value = f"{ctx.author.mention}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🍺")
        await asyncio.sleep(10)
        users = await msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))
        if len(users) == 0:
            em = discord.Embed(title = '<:fail:761292267360485378> Beer Party Failed', color = ctx.author.color)
            em.add_field(name = "Reason:", value = "No one joined D:")
            em.add_field(name = "Next steps:", value = "Dont make a party which you don't enter!")
            await ctx.channel.send(embed = em)
            return        
        msg = f"```diff\n+ {ctx.author.name} hosts a beer party\n\n"
        for user in users:
            died = random.randint(0, 1)
            if died == 0:
                msg += f"- {ctx.name} died cause of drinking too much\n"
            if died == 1:
                msg += f"- {user.name} had a nice time at the bar\n"
        msg += "```"

    @coinflip.error
    async def coinflip_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = 'Flipping coins is boring, stop wasting your time!')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @random_number.error
    async def random_number_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = 'Random numbers are boring, stop wasting your time m8!')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp random_number <range1> <range2>\n- imp random_number 29\n```")
            em.add_field(name = "Description:", value = "Put all the required arguments next time!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @thank.error
    async def thank_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*sighs there is a cooldown for everything*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp thank @NightZan999 made TheImperialGod\n- imp thank NoobLance made my coffee\n```")
            em.add_field(name = "Description:", value = "Mention a member to thank them!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*sighs there is a cooldown for everything*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @eightball.error
    async def eightball_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*stop looking at the future, cause ur soon gonna be there!*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp eightball will I invite this bot to my server?\n- imp eightball\n```")
            em.add_field(name = "Description:", value = "Put all the required arguments next time!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @poll.error
    async def poll_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*make decisions rather than being a sheep!*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp poll <message>\n- imp poll\n```")
            em.add_field(name = "Description:", value = "Put all the required arguments next time!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @show_toprole.error
    async def show_toprole_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*sighs there is a cooldown for everything*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp show_toprole @NightZan999\n- imp show_toprole Nooblance\n```")
            em.add_field(name = "Description:", value = "Mention a member to see their toprole them!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @_pass.error
    async def _pass_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*password rush eh?*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp _pass <amountOfCharacters>\n- imp _pass NightZan999\n```")
            em.add_field(name = "Description:", value = "Type the amount of characters in your password as an integer!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)


    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*sighs there is a cooldown for everything*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\nimp avatar @NightZan999 such a beatiful avatar\n- imp avatar dog cringe\n```")
            em.add_field(name = "Description:", value = "Mention a member to see their avatar!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @respect.error
    async def respect_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = '*sighs there is a cooldown for everything*')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @beer.error
    async def beer_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = 'if you go drunk, you die and lose all your coins dude')
            em.add_field(name = "Try again in:", value = "`{:.2f}`s".format(error.retry_after))
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = '<:fail:761292267360485378> You missed Arguments!', color = ctx.author.color)
            em.add_field(name = "Usage:", value = "```diff\n+ imp beer @NightZan999 epic\n- imp beer myFriendName haha\n```")
            em.add_field(name = "Description:", value = "Mention a member to have beer with them!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Utils(client))