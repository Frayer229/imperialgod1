import discord
from discord.ext import commands
import json

class GuildEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("GuildEvents are ready!")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        # send the log in support server
        with open("./config.json", "r") as f:
            config = json.load(f)
        serverId = int(config["IDs"]["serverLogId"])
        channelId = int(config["IDs"]["channelLogId"])

        embed = discord.Embed(title = "I joined a new server!", color = discord.Color.red())
        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(self.client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(self.client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")


        sguild = self.client.get_guild(serverId)
        for channel in sguild.channels:
            if channel.id == channelId:
                await channel.send(embed = embed)
                break
        # now send a message to the people, for the people.
        em = discord.Embed(title = "<:VERIFIED_DEVELOPER:761297621502656512> Thanks for adding me to your server!",color = discord.Color.red(), description = f"""I am TheImperialGod, Lord of the empire who will bring peace to your server: {guild.name}.\n
I see that you have {guild.member_count} members, how about we try to double that in the next week!\n\nSO to get started with my power, please use `imp help`. My prefix is `imp` and `imp help` shows you all the commands.\n\n\nHere is what I can do:```diff\n+ Make your members contact you via tickets\n+ Create roles for you\n+ Can set an autorole\n+ Can do maths for you!\n+ Host giveaways\n+ Make people rich with server economy\n- Can show you information about users and the server!\n- Make you have fun with my utilities\n- Show you images and memes from reddits\n``` """)
        em.set_author(name = "TheImperialGod")
        em.set_footer(text = "Thanks for inviting me!", icon_url = guild.icon_url)
        if guild.system_channel is not None:
            await guild.system_channel.send(embed = em)
        else:
            for channel in guild.channels:
                return await channel.send(embed = em)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("./config.json", "r") as f:
            config = json.load(f)
        serverId = int(config["IDs"]["serverLogId"])
        channelId = int(config["IDs"]["channelLogId"])

        embed = discord.Embed(title = "I left a new server!", color = discord.Color.red())
        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(self.client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(self.client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")


        sguild = self.client.get_guild(serverId)
        for channel in sguild.channels:
            if channel.id == channelId:
                await channel.send(embed = embed)
                break
        
        # dm the owner about it
        try:
            await guild.owner.send("""I hope I was of service to you in your server! I would love to hear your feedback on my top.gg page: https://top.gg/bot/768695035092271124/ """)
        except:
            pass

def setup(client):
    client.add_cog(GuildEvents(client))
