"""
MIT LICENCE 2020 - 2021
All the code and the full bot is nothing but TheImperialGod
All the code is made by NightZan999, check him out at https://github.com/NightZan999
The deposit and withdraw command have been added on to by Makiyu-py, he used it in a fork
The repository the code has been taken from is at https://github.com/NightZan999/TheImperialGod

Be sure to have this in your project at the beginning!
"""
import discord #discord object
from discord.ext import commands, tasks #commands from external
import random #random
import json
import os
import asyncio

def load_cogs(): #loading all our cogs
    cogs = [
        "cogs.info.help", # help command
        "cogs.fun.animals", # searching reddit
        "cogs.economy.bankcommands", # bank commands in economy
        "cogs.economy.moneymaking", # moneymaking commands in economy
        "cogs.economy.shop", # making a shop with database in economy!
        "cogs.economy.gambling", # gambling commands
        "cogs.fun.misc", # misc commands
        "cogs.fun.utils", # utilities
        "cogs.info.info", # information
        "cogs.info.math", # math commands
        "cogs.moderation.giveaways", # giveaway commands!
        "cogs.moderation.mod", # moderation commands
        "cogs.owner.owner", # owner commands
        "cogs.tickets.tickets", # ticket commands
        "cogs.info.topgg", # has top.gg stuff bois!
        "cogs.exclusive.exclusive", # has exclusive commands
        "cogs.moderation.autorole", # autoroles
        "cogs.music.music", # music :D
        "cogs.info.minecraft", # minecraft commands
        "cogs.points.points", # points
        "cogs.owner.patch" # patching stuff
    ]
    
    for cog in cogs:
        client.load_extension(cog)

    events = [
        "events.GuildEvents", # when the bot leaves or joins a guild!
        "events.ReactionAdd",
        "events.ReactionRemove",
        "events.OnCommand",
        "cogs.points.pointevents"
    ]

    for event in events:
        client.load_extension(event)
    print("===============================")
    print(f"{len(cogs)} cogs are loaded\n{len(events)} events are loaded")  
    # now load jishaku
    client.load_extension("jishaku")
    print("Jishaku has been loaded!\n===============================")

with open("config.json", "r") as f:
    config = json.load(f)

#consts
BOT_TOKEN = config["token"]
CLIENT_ID = config["clientId"]
CLIENT_SECRET = config["clientSecret"]
PUBLIC_KEY = config["publicKey"]
BOT_PREFIX = config["prefix"]
new_link ="https://discordapp.com/oauth2/authorize?&client_id=".join(str(CLIENT_ID))
new_link.join("&scope=bot&permissions=21474836398")

# custom client
class TheImperialGod(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print("Ready!")
        print("Username: ", client.user.name)
        print("User ID: ", client.user.id)
        print("----------------------------")

    async def get_cogs(self):
        return cogs
    
    async def get_events(self):
        return events
    
    async def get_all_emojis(self):
        return Emojis
    
    async def read_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    
    async def write_json(self, output, filename):
        with open(filename, "w") as f:
            return json.dump(output, f)

intents = discord.Intents.all()
client = TheImperialGod(command_prefix = ['imp ', 'Imp ', 'iMp ', 'IMp ', 'imP ', 'ImP ', 'iMP ', 'IMP '], case_insensitive = True, intents = intents, allowed_mentions = discord.AllowedMentions(everyone = False, users = True, roles = True, replied_user = True)) #making a client object

async def ch_pr(): #changing the bots status every 5 secs!!!
    await client.wait_until_ready()
    while not client.is_closed():
        statuses = [
            f"The Protection of {len(client.guilds)} servers",
            "imp help | imp support 😋"
        ]
        status = random.choice(statuses)
        await client.change_presence(activity = discord.Streaming(name = status, url = "https://twitch.tv/pewdiepie"))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    try:
        if message.content == "<@!768695035092271124>":
            em = discord.Embed(title = "Help for TheImperialGod", color = message.author.color,
            description = "Check some information about me!")
            em.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)
            em.add_field(name = "What can I do?", value = "I can make your server so charming! Whether you are a moderator or not!")
            em.add_field(name = "Commands:", value = "Check out `imp help` for a list of my commands")
            em.add_field(name = "Prefix:", value = "My prefix is `imp`")
            em.add_field(name = "Command Types", value = "Economy, Moderation, Information, Utilities, Math, Fun, Giveaways, Tickets, Miscellanous")
            em.add_field(name = "Website:", value = "[Click Here](https://nightzan.ml/projects/theimperialgod/index.html)")
            em.set_footer(text = "© TheImperialGod™ v1.5.1",icon_url = self.client.user.avatar_url)
            em.set_thumbnail(url = message.author.avatar_url)
            await message.channel.send(embed = em)
    except:
        pass

    await client.process_commands(message)


load_cogs()
client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)
