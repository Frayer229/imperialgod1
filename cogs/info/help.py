import discord
from discord.ext import commands
import asyncio
import random

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.help_pages = []
        self.gaws_commands = [
            'gstart',
            'reroll'
        ]
        self.misc_commands = [
            'invite',
            'show_toprole',
            'avatar',
            'candy',
            "hypesquad",
            "support"
            ]
        self.economy_commands = [
            "Withdraw",
            "Balance",
            "Deposit",
            "Slots"
            'Rob',
            'Dice',
            'Leaderboard',
            'Daily',
            'Weekly'
            ]
        self.tips = [
            "Did you know that TheImperialGod has an economy system!",
            "Did you know that TheImperialGod was made by NightZan999?",
            "Did you know that TheImperialGod was coded in a language called Python!",
            "Did you know that TheImperialGod has over 45,000 lines of code if put in one file!",
            "Did you know that TheImperialGod has tickets!"
        ]

    def addPage(self, embed : discord.Embed):
        self.help_pages.append(embed)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help command ready!")

    @commands.group(invoke_without_command = True)
    async def help(self, ctx, category = None):
        # create pages and add them to the help_pages
        page1 = discord.Embed(title = "Help", color = ctx.author.color, description = f"""
        **Type `imp help` and then a __category__ for more information for even more information!**\n
        My prefix is `imp`
        """)
        page1.add_field(name = f":dollar: Economy Commands: [9]", value = "`Balance`, `Beg`, `Withdraw`, `Deposit`, `Give`, `Serve`, `Daily`, `Weekly`, `Bet`, `claimrewards vote`")
        page1.add_field(name = f"<:Coder_Hammer:826315685142462474> Moderation Commands: [19]", value = "`Kick`, `Ban`, `Softban`, `Purge`, `Lock`, `Unlock`, `Mute`, `Unmute`, `Unban`, `createrole`, `Announce`, `nick`, `setmuterole`, `setautorole`, `addrole`, `removerole`, `deleterole`")
        page1.add_field(name = f"<:info:761298826907746386> Information Commands: [8]", value = f"`userinfo`, `avatar`, `serverinfo`, `whois`, `channelinfo`, `botinfo`,`show_toprole`, `credits`")
        page1.add_field(name = f":tools: Utilities: [12]", value = "`coinflip`, `random_number`, `code`, `thank`, `reverse`, `8ball`, `poll`, `show_toprole`, `passwordgenerator`, `avatar`, `respect`, `beer`, `guess`")
        page1.add_field(name = f"<:pepethink:791969112771395625> Math Commands [7]:", value = f"`add`, `subtract`, `multiply`, `divide`, `square`, `sqrt`, `pow`")
        page1.add_field(name = f':video_game: Fun: [12]', value = f"`dog`, `cat`, `duck`, `fox`, `panda`, `koala`, `tiger`, `lion`, `snake`, `redpanda`, `owl`, `meme`, `joke`")
        page1.add_field(name = f":gift: Giveaways: [2]", value = "`gstart`, `reroll`")
        page1.add_field(name = f":ticket: Imperial Tickets [4]", value = f"`new`, `close`, `addticketrole`, `setticketlogs`")
        page1.add_field(name = f":question: Misc: [{len(self.misc_commands) - 1}]", value = "`invite`,  `avatar`, `candy`, `suggest`, `support`")
        page1.set_footer(text = f"Page (1 / 3)")
        page1.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
        self.addPage(page1)

        page2 = discord.Embed(title = "Help",color = ctx.author.color, description = f"""
        **Type `imp help` and then a __category__ for more information for even more information!**\n
        My prefix is `imp`
        """)
        page2.add_field(name = "<:zancool:819065864153595945> Exclusive Commands [1]", value = '`claimrewards`')
        page2.add_field(name = "<:goldingot:818413753581699102> Minecraft Commands [2]", value = "`mcstats`, `mchistory`")
        page2.add_field(name = ":notes: Music Commands [5]", value = "`join`, `leave`, `play`, `resume`, `pause`")
        page2.add_field(name = ':trophy: Levelling Commands [4]', value = '`points`, `givepoints`, `pointsper`, `pointshelp`')
        page2.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
        page2.set_footer(text = f"Page (2 / 3)")
        self.addPage(page2)
        # add our last page
        page3 = discord.Embed(title = "Help Center and Links", color = ctx.author.color,
        description = """<:invite:761292264857141288> [Invite](https://discord.com/oauth2/authorize?client_id=768695035092271124&scope=bot&permissions=21474836398)\n
        :radioactive: [Top.gg](https://top.gg/bot/768695035092271124)\n
        :scorpius: [Vote](https://top.gg/bot/768695035092271124/vote)\n
        <:info:761298826907746386> [Support Server](https://discord.gg/KuPzxqHe)\n
        <:VERIFIED_DEVELOPER:761297621502656512> [Web Dashboard](https://theimperialgod.ml)
        """
        )
        page3.add_field(name = 'Required Arguments', value = "<> = means a required argument!\n[] = means an optional argument!")
        page3.add_field(name = 'Embed Info', value = "If no response is detected we will clear all reactions!")
        page3.add_field(name = "Tip :coin::", value =f"**{random.choice(self.tips)}**")
        page3.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
        page3.set_footer(text = f"Page (3 / 3)")
        self.addPage(page3)
        # create emojis
        buttons = [
            "⏮️",
            "⬅️",
            "🔐",
            "➡️",
            "⏭️"    
        ]
        current = 0
        msg = await ctx.send(embed = self.help_pages[current])

        for button in buttons:
            await msg.add_reaction(button)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in buttons

        # no blocking
        # async works for a reason :D
        while True: 
            try:
                reaction, user = await self.client.wait_for("reaction_add", check = check, timeout = 300)
            
            except asyncio.TimeoutError:
                await msg.clear_reactions()
                return
            else:
                previous_page = current

                if str(reaction.emoji) == "⏮️":
                    current = 0
                    button = buttons[0]
                    await msg.remove_reaction(button, ctx.author)
                
                elif str(reaction.emoji) == "⬅️":
                    if current != 0:
                        current -= 1
                    else:
                        current = len(self.help_pages) - 1
                    button = buttons[1]
                    await msg.remove_reaction(button, ctx.author)
                
                elif str(reaction.emoji) == "➡️":
                    if current < len(self.help_pages) - 1:
                        current += 1
                    else:
                        current = 0
                    button = buttons[3]
                    await msg.remove_reaction(button, ctx.author)
                
                elif str(reaction.emoji) == "⏭️":
                    current = len(self.help_pages) - 1
                    button = buttons[4]
                    await msg.remove_reaction(button, ctx.author)

                elif str(reaction.emoji) == "🔐":
                    await msg.clear_reactions()
                    return

                if current != previous_page:
                    await msg.edit(embed = self.help_pages[current])
    
    @help.command(aliases=["information"])
    async def info(self, ctx):
        em = discord.Embed(title = "Help Information", color = ctx.author.color)
        em.add_field(name=  "Userinfo", value = "Shows you information about a user!")
        em.add_field(name = "Avatar", value = "Shows someones profile picture in a zoomed format!")
        em.add_field(name = "Serverinfo", value = "Shows you information about the server!")
        em.add_field(name = "Whois", value = "Shows you whois a person!")
        em.add_field(name = 'Botinfo', value = 'Shows you information about me!')
        em.add_field(name = "Show_toprole", value = "Shows you a toprole of a user!")
        em.add_field(name = 'Credits', value ="Shows you **everyone who contributed to TheImperialGod**")
        await ctx.send(embed = em)

    @help.command(aliases= ["eco"])
    async def economy(self, ctx):
        em = discord.Embed(title = 'Help Economy', color =ctx.author.color)
        em.add_field(name = "Balance", value = "Check the balance of a user!")
        em.add_field(name = "Beg", value = "Beg and make money!")
        em.add_field(name = "Serve", value = "Serve your server and make some coins")
        em.add_field(name = "Withdraw", value = "Withdraw some coins from your bank!")
        em.add_field(name=  "Deposit", value = "Deposit some coins into your bank!")
        em.add_field(name= "Daily", value = "Get daily rewards")
        em.add_field(name = "Weekly", value = "Get weekly rewards")
        em.add_field(name = "Bet", value = "Bet some money!")
        em.add_field(name = "claimrewards vote", value = "Claim some rewards for voting for me!")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction('💰')

    @help.command(aliases=["mod"])
    async def moderation(self, ctx):
        em = discord.Embed(title = 'Help Moderation', color =ctx.author.color)
        em.add_field(name = "Kick", value = "Kick a user")
        em.add_field(name = "Ban", value = "Ban a user")
        em.add_field(name = "Purge", value = "Delete tons of messages quickly")
        em.add_field(name = "Lock", value = "Lock a channel")
        em.add_field(name=  "Unlock", value = "Unlock a channel")
        em.add_field(name= "Unban", value = "Unban a user")
        em.add_field(name = "Warn", value = "Warn a user")
        em.add_field(name = "Addrole", value = "Give a role")
        em.add_field(name = "Removerole", value = "Remove a role from a user")
        em.add_field(name = "Setdelay", value = "Sets a **custom slowmode in the channel**")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg  = await ctx.send(embed = em)
        await msg.add_reaction("🗡")

    @help.command(aliases = ["utilities"])
    async def utils(self,ctx):
        em = discord.Embed(title = "Help Utils:", color = ctx.author.color)
        em.add_field(name = "Coinflip", value = "Flips a coin!")
        em.add_field(name = "random_number", value = "Returns a random number in 2 given ranges")
        em.add_field(name = "code", value = "Encodes a message and turns it into code")
        em.add_field(name = "Thank", value = "Thanks a user, for something that they have done!")
        em.add_field(name = "Reverse", value = "Reverses your message!")
        em.add_field(name = "8ball", value = "Predicts the future!")
        em.add_field(name = "poll", value = "Creates a poll!")
        em.add_field(name = "show_toprole", value = "Shows a users toprole")
        em.add_field(name ="passswordgenerator", value = "Generates you a random password and DMs it!")
        em.add_field(name = "avatar", value = "Check beatufiul avatars!")
        em.add_field(name= "Respect", value = "Respect something!")
        em.add_field(name = "Beer", value = "Have beer with someone!")
        em.add_field(name = "Guess", value = "Play a guess game with me boi!")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🍩")
        
    @help.command(aliases=['miscellaneous'])
    async def misc(self, ctx):
        em = discord.Embed(title = "Help Misc:", color = ctx.author.color)
        em.add_field(name = "invite", value = "Get a link to invite the bot to your s")
        em.add_field(name = "show_toprole", value = "Shows the top role of a person")
        em.add_field(name = "passwordgenerator", value = "DMs you a random password, you can also specify how many letters!")
        em.add_field(name = "botinfo", value = "Shows general information about the Bot!")
        em.add_field(name = "serverinfo", value = "Shows you information about your server!")
        em.add_field(name = "userinfo", value = "Shows you information about a user")
        em.add_field(name = "channelinfo", value = "Shows you information about a channel!")
        em.add_field(name = "avatar", value = "Shows you an avatar of a person")
        em.set_footer(text='Bot Made by NightZan999#0194')
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🐬")

    @help.command(aliases=["ticket"])
    async def tickets(self, ctx):
        em = discord.Embed(title = "Help Tickets", color = ctx.author.color,
        description = """Tickets are the easiest way for members getting their answers via the staff!\n
        A user types `imp new [reason]` and gets a private channel only, the user, the owner and a role can get access to.\n
        Conversations are completely safe and we respect your privacy. To fully setup tickets see the commands!
        """)
        em.add_field(name = "New", value = "Creates a new ticket")
        em.add_field(name = "Close", value = 'Deletes a ticket')
        em.add_field(name = "Addticketrole", value = "Add a role which can access tickets")
        em.add_field(name = "Setticketlogs", value = "Set a log channel, which tells you when an action related to tickets happens!")
        em.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed  = em)

    @help.command(aliases=["mathematics", 'mafs', "maf", "maths"])
    async def math(self, ctx):
        em = discord.Embed(title = "Help Mafs", color = ctx.author.color, description = """
        I decided to make maths a part of this discord bot, as
        many times people in discord would have mathematic applications 
        and I want people who are not skilled to do maths to let us do it for you!
        Quick mafs bois!
        """)
        em.add_field(name = "add", value = 'Add two numbers!')
        em.add_field(name = "subtract", value = 'Subtract two numbers!')
        em.add_field(name = "multiply", value = 'Multiply two numbers!')
        em.add_field(name = "divide", value = 'Divide two numbers!')
        em.add_field(name = "square", value = 'Square 1 number!')
        em.add_field(name = "sqrt", value = 'Squareroot 1 number!')
        await ctx.send(embed = em)
    
    @help.command(aliases=["gaws", "giveaway", "gaw"])
    async def giveaways(self, ctx):
        em = discord.Embed(title = "Help Giveaways", color = ctx.author.color,description = "Giveaway Bots are quite rare, but you are lucky to have me! An all in one!")
        em.add_field(name = "gstart", value = 'Interactive setup of giveaways!')
        em.add_field(name = "reroll", value = f"Rerolls a giveaway, format: ```diff\n+ imp reroll <channel> <messageId>\n- imp reroll <messageId>```")
        msg = await ctx.send(embed = em)
        await msg.add_reaction("🎉")

    @help.command()
    async def exclusive(self, ctx):
        des ="""Exclusive commands are commands in which you have to vote for me or support me in any way to get access to some commands!\n
        This is because we want people to get a ton of stuff but we also need credit for the work. Hope you understand!
        """
        em = discord.Embed(title = "<:zancool:819065864153595945> Exclusive Commands", color = ctx.author.color, description = des)
        em.add_field(name = "claimrewards", value = "This is a command group, if invoked with no subcommand it will give you a list of rewards to claim!")
        await ctx.send(embed = em)

def setup(client):
    client.remove_command("help")
    client.add_cog(Help(client))
