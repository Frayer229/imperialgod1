import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json

class Autorole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Autorole is ready!")
    
    @commands.command()
    @has_permissions(manage_roles = True)
    async def setautorole(self, ctx, role : discord.Role = None, *, reason = None):
        roles = await self.get_roles()
        await self.add_autorole(ctx.guild, role)

        em = discord.Embed(title = "<:success:761297849475399710> Auto Role Set", color = ctx.author.color, description = f"{role.mention} was successfully set as the auto role!")
        em.add_field(name= "Role:", value = f"{role.mention}")
        em.add_field(name = "Reason:", value = f"`{reason}`")
        em.add_field(name = "Moderator:", value = f"{ctx.author.mention}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "this autorole goes to new members only tho", icon_url = ctx.author.avatar_url)
        return await ctx.send(embed = em)

    @setautorole.error 
    async def setautorole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Auto Role Failed!",color=ctx.author.color, description = "The Command Auto Role failed!")
            em.add_field(name = "Reason:", value = "Permissions Missing!")
            em.add_field(name = "Moderator:", value = f"{ctx.author.mention}")
            em.set_footer(text = "this autorole goes to new members only tho", icon_url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            return await ctx.send(embed = em)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        roles = await self.get_roles()
        guild = member.guild 
        if str(guild.id) not in roles:
            return 
        
        else:
            role_id = int(roles[str(guild.id)]["autorole"])
            try:
                role = await guild.get_role(role_id)
                await member.add_roles(role)
            except:
                return

    # helper functions
    async def get_roles(self):
        with open("./data/mod.json", "r") as f:
            data = json.load(f)
        return data 
    
    async def add_autorole(self, guild, role : discord.Role):
        roles = await self.get_roles()
        if str(guild.id) not in roles:
            roles[str(guild.id)] = {}
            roles[str(guild.id)]["autorole"] = int(role.id)
        else:
            roles[str(guild.id)]["autorole"] = int(role.id)

        await self.update_db(roles)
        return True

    async def update_db(self, dict):
        with open("./data/mod.json", "w") as f:
            json.dump(dict, f)
        return True


def setup(client):
    client.add_cog(Autorole(client))