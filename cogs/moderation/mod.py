import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions, BadArgument

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    @has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member = None, *, reason = None):
        try:
            if member == None:
                embed = discord.Embed(title = "<:fail:761292267360485378> Kick Failed!", color= ctx.author.color)
                embed.add_field(name = "Reason:", value = "Ping a user to kick them!")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            if member == ctx.author:
                em = discord.Embed(title = '<:fail:761292267360485378> Kick Failed', color = ctx.author.color)
                em.add_field(name = 'Reason:', value = f"You can't kick yourself ;-;")
                em.add_field(name = "Next Steps:", value = "Try to kick someone else idunno")
                em.set_footer(text = "imagine kicking urself, couldn't be me!")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=  em)
                return
            try:
                await member.send(f"You were kicked in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")
            except:
                pass
            await member.kick(reason = reason)
            em = discord.Embed(title = f"<:success:761297849475399710> Kick was successful!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen, we got ||{member.mention}|| out of the server!")
            em.add_field(name = f"Member:", value = f"`{member.name}`")
            em.add_field(name = "Reason: ", value = f"`{reason}`")
            em.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
            em.set_footer(text = f"{member.name} said bye!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        except:
            em = discord.Embed(title = "<:fail:761292267360485378> Kick Failed!", color = discor.Color.red())
            em.add_field(name = 'Reason', value =f"{member.mention} is a moderator or an admin!")
            em.add_field(name = "Contact support!", value = "This could also be due to the hierarchy!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Kick Failed!", color = ctx.author.color, description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = "Reason:", value = "`Kick members Permission Missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Kick Failed!", color = ctx.author.color, description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = "Reason:", value = "`Ping a user to kick them!`")
            em.add_field(name=  "Usage:", value = "```diff\n+ imp kick @NightZan999 swear words\n- imp kick someonesName swearing\n```")
            em.set_footer(text = "Kick properly already!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            

    @commands.command(aliases=["giverole", "addr"])
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member : discord.Member = None, role : discord.Role = None,*,reason = None):
        if member is None:
            embed = discord.Embed(title = "<:fail:761292267360485378> Addrole Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "Ping a user to give them a role them!")
            embed.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        if role is None:
            embed = discord.Embed(title = "<:fail:761292267360485378> Addrole Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "Ping a role to give {} that role!".format(member.mention))
            embed.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        try:
            addRole = True
            for role_ in member.roles:
                if role_ == role:
                    addRole = False
                    break
            if not addRole:
                embed = discord.Embed(title = "<:fail:761292267360485378> Add Role Failed!", color= ctx.author.color)
                embed.add_field(name = "Reason:", value = "I was unable to add that role to {}!".format(member.mention))
                embed.add_field(name = "Why?",value = f"{member.mention} already has {role.mention}, so...")
                embed.set_footer(text = "-_-")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                em = discord.Embed(title=  "<:success:761297849475399710> Add Role Successful!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we gave {member.mention} the role {role.mention}")
                em.add_field(name = "Reason:", value = f"`{reason}`")
                em.add_field(name = "User:", value = f"{member.mention}")
                em.add_field(name = "Role:", value = f"{role.mention}", inline = True)
                em.add_field(name ="Moderator:", value = f"{ctx.author.mention}", inline = False)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = em)
                await member.add_roles(role)
                return
        except:
            embed = discord.Embed(title = "<:fail:761292267360485378> Addrole Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "I was unable to give {} that role!".format(member.mention))
            embed.add_field(name = "Why?",value = "This is usually because of role hierarchy or because I don't have manage roles permissions!")
            embed.set_footer(text = "-_-, gimme the perms m8")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
    
    @commands.command(aliases=["takerole", "remover"])
    @commands.guild_only()
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member : discord.Member = None, role : discord.Role = None,*,reason = None):
        if member is None:
            embed = discord.Embed(title = "<:fail:761292267360485378> Removerole Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "Ping a user to take away a role from them!")
            embed.set_footer(text = "-_-")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        if role is None:
            embed = discord.Embed(title = "<:fail:761292267360485378> Removerole Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "Ping a role to remove that role from {}!".format(member.mention))
            embed.set_footer(text = "-_-")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        try:
            roleRemoved = False
            for role_ in member.roles:
                if role_ == role:
                    await member.remove_roles(role)
                    roleRemoved = True
                    return
            if not roleRemoved:
                embed = discord.Embed(title = "<:fail:761292267360485378> Remove Role Failed!", color= ctx.author.color)
                embed.add_field(name = "Reason:", value = "I was unable to remove that role from {}!".format(member.mention))
                embed.add_field(name = "Why?",value = f"{member.mention} doesn't even have {role.mention}, so...")
                embed.set_footer(text = "-_-")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            else:
                em = discord.Embed(title=  "<:success:761297849475399710> Remove Role Successful!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we removed the role {role.mention} from {member.mention}")
                em.add_field(name = "Reason:", value = f"`{reason}`")
                em.add_field(name = "User:", value = f"{member.mention}")
                em.add_field(name = "Role:", value = f"{role.mention}", inline = True)
                em.add_field(name ="Moderator:", value = f"{ctx.author.mention}", inline = False)
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = em)
                return
        except:
            embed = discord.Embed(title = "<:fail:761292267360485378> Remove Role Failed!", color= ctx.author.color)
            embed.add_field(name = "Reason:", value = "I was unable to remove that role from {}!".format(member.mention))
            embed.add_field(name = "Why?",value = "This is usually because of role hierarchy or because I don't have manage roles permissions!")
            embed.set_footer(text = "-_-, gimme the perms m8")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Add Role Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Manage Role Permission Missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Add Role Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Ping a user and a role to give the role to the user!`")
            em.add_field(name = "Format:", value = f'```diff\n+ imp addr <@member> <@role> [reason]\n- imp addrole <@role> [reason] <@member>\n```')
            em.set_footer(text = "Addrole properly already!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)


    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Remove Role Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Manage Role Permission Missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Remove Role Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Ping a user and a role to remove the role from the user!`")
            em.add_field(name = "Format:", value = f'```diff\n+ imp removerole <@member> <@role> [reason]\n- imp removerole <@role> [reason] <@member>\n```')
            em.set_footer(text = "Remove Role properly already!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
    
    @commands.command()
    @commands.guild_only()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member = None, *,reason = None):
        try:
            if member == None:
                embed = discord.Embed(title = "<:fail:761292267360485378> Ban Failed!", color= ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we, uhh wait there was no member specified")
                embed.add_field(name = "Reason:", value = "Ping a user to ban them!")
                embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed = embed)
                return
            if member == ctx.author:
                em = discord.Embed(title = '<:fail:761292267360485378> Ban Failed', color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we ||wait this is you, you buffoon||")
                em.add_field(name = 'Reason:', value = f"You can't ban yourself ;-;")
                em.add_field(name = "Next Steps:", value = "Try to ban someone else idunno")
                em.set_footer(text = "imagine banning urself, couldn't be me!")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                await ctx.send(embed=  em)
                return
            try:
                await member.send(f"You were banned in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")
            except:
                pass
            await member.ban(reason = reason)
            em = discord.Embed(title = f"<:success:761297849475399710> Ban was successful!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we gottem")
            em.add_field(name = f"Victim:", value = f"`{member.name}`")
            em.add_field(name = "Reason: ", value = f"`{reason}`")
            em.add_field(name = "**Moderator**:", value = f"`{ctx.author.name}`")
            em.set_footer(text = f"{member.name} said bye!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

        except:
            em = discord.Embed(title = "<:fail:761292267360485378> Ban Failed!", color = discor.Color.red(), description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we uhhhhhhh damn-")
            em.add_field(name = 'Reason', value =f"{member.mention} is a moderator or an admin!")
            em.add_field(name = "Contact support!", value = "This could also be due to the hierarchy!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Ban Failed!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we-")
            em.add_field(name = "Reason:", value = "`Ban members Permission Missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Ban Failed!", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> Ladies and gentlemen we go-")
            em.add_field(name = "Reason:", value = "`Ping a user to Ban them!`")
            em.add_field(name = "Usage:", value = "```diff\n+ imp ban @NightZan999 DM adverts\n- imp ban someonesName DM adverts\n```")
            em.set_footer(text = "Ban properly already!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_channels = True)
    async def announce(self,ctx, channel : discord.TextChannel, *, msg = None):
        embed = discord.Embed(title = "Announcement!", color = ctx.author.color)
        embed.add_field(name = "Announcement:", value = f"`{msg}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.autor.name}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await channel.send(embed = embed)

    @announce.error
    async def announce_error(self,ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Announcement failed!", color = ctx.author.color)
            embed.add_field(name = 'Reason:', value = "Some perms are missing")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(title = "<:fail:761292267360485378> Announcement failed!", color = ctx.author.color)
            embed.add_field(name = 'Reason:', value = f"Mention a channel properly! And write a message after it!")
            embed.add_field(name = "Usage", value = "```diff\n+ imp announce #announcements We are getting react roles :D\n- imp announce channelID we are closing the server D:```\n")
            embed.set_footer(text = 'Do stuff properly!')
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def createrole(self, ctx, *, name = "UnknownRole"):
        role=  await ctx.guild.create_role(name = name)
        em = discord.Embed(title = "<:success:761297849475399710> Role Created", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> {role.mention} was successfully created!")
        em.add_field(name = "Role:", value = f"{role.mention}")
        em.add_field(name ="Moderator:", value = f"{ctx.author.mention}")
        em.set_footer(text = "Good job creating roles!")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @createrole.error
    async def createrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Role Creation Failed")
            em.add_field(name = "Reason:", value = "`Manage Roles perms missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases=["delrole"])
    @commands.guild_only()
    @commands.has_permissions(manage_roles = True)
    async def deleterole(self, ctx, *, role: discord.Role):
        em = discord.Embed(title = "<:success:761297849475399710> Role Deleted", color = ctx.author.color, description = f"<:Coder_Hammer:826315685142462474> {role.mention} was successfully deleted!")
        em.add_field(name = "Role:", value = f"{role.mention}")
        em.add_field(name ="Moderator:", value = f"{ctx.author.mention}")
        em.set_footer(text = "o wow")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

        await role.delete(reason = f"{ctx.author.name} asked for it!")

    @deleterole.error
    async def deleterole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Role Deletion Failed")
            em.add_field(name = "Reason:", value = "`Manage Roles perms missing!`")
            em.set_footer(text = "Imagine thinking you have the perms!")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod commands Loaded!")

    @commands.command(aliases = ["purge", "massdelete", "bulkdel"])
    @commands.guild_only()
    @has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 1):
        try:
            amount = int(amount)
        except:
            await ctx.send("Provide an integer amount of messages!")
            return 
        await ctx.channel.purge(limit = amount)

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Purge Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"`Manage Messages Permissions Missing!`")
            embed.set_footer(text = "Imagine thinking you have the perms!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def lock(self, ctx, *, reason = None):
        channel = ctx.channel
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
        em = discord.Embed(title = f"<:success:761297849475399710> Channel has been locked!", color = discord.Color.green(), description = f"<:Coder_Hammer:826315685142462474> {channel.mention} was successfully locked!")
        em.add_field(name = "**Responsible Moderator:**", value = f"`{ctx.author.name}`")
        em.add_field(name = "**Reason:**", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.channel.send(embed = em)

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Lock Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            embed.set_footer(text = "Imagine thinking you have the perms!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def unlock(self, ctx, *, reason = None):
        channel = ctx.channel
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        em = discord.Embed(title = f"<:success:761297849475399710> Channel has been unlocked!", color = discord.Color.green(), description = f"<:Coder_Hammer:826315685142462474> {channel.mention} was successfully unlocked!")
        em.add_field(name = "**Responsible Moderator:**", value = f"`{ctx.author.name}`")
        em.add_field(name = "**Reason:**", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.channel.send(embed = em)

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "<:fail:761292267360485378> Unlock Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            embed.set_footer(text = "Imagine thinking you have the perms!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def setdelay(self, ctx, amount = 5, *, reason = None):
        if amount > 6000:
            await ctx.channel.send("Amount needs to be less than 6000!")
            return
        try:
            amount = int(amount)
        except:
            em = discord.Embed(title = "<:fail:761292267360485378> Set Delay Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Amount is not an integer")
            em.add_field(name = "Usage:", value = "```diff\n+ imp setdelay 10 chat active for a change\n- imp setdelay no you\n```")
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            return
        
        if ctx.channel.slowmode_delay != amount:
            await ctx.channel.edit(slowmode_delay=amount)
        else:
            embed = discord.Embed(title = "Setdelay Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"The channels slowmode is already `{amount}`!")
            embed.set_footer(text = "Imagine wasting time!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
            return
        em = discord.Embed(title = "<:success:761297849475399710> Change in channel settings", color = ctx.author.color)
        em.add_field(name = "**Responsible Moderator:**", value = f"`{ctx.author.name}`")
        em.add_field(name = "**Reason:**", value = f"`{reason}`")
        em.add_field(name=  "Description", value = f"Now the channel has a slowmode which avoids spamming\n {ctx.author.mention} for more type `imp lock [reason]`", inline = False)
        em.add_field(name = "Slowmode", value = f"`{amount} seconds`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @setdelay.error
    async def setdelay_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Setdelay Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            embed.set_footer(text = "Imagine thinking you have the perms!")
            embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = embed)
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    @has_permissions(ban_members = True)
    async def unban(ctx, member : str, *, reason = None):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split("#")

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                embed = discord.Embed(title = f"{member_name} was unbanned!", color = ctx.author.color)
                embed.add_field(name = "Reason:", value = f"`{reason}`")
                embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
                await ctx.send(embed = embed)
                return

        await ctx.send("Not a valid user, try it like this:\n`imp unban name#disc`")

    #normal function
    def convert(self, time):
        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    @commands.command()
    @commands.guild_only()
    @has_permissions(manage_channels = True)
    async def count(self,ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        messages = await channel.history(limit = None).flatten()
        count = len(messages)
        em = discord.Embed(title = f"Count of {channel.mention}", color = ctx.author.color, description = "There are {} messages in {}".format(count, channel.mention))
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed=em)
    
    @count.error
    async def count_error(self, ctx, error):
        if isinstance(error, commands.BotMissingPermissions):
            em = discord.Embed(title = f'<:fail:761292267360485378> {ctx.command.name} Failed!', color = discord.Color.random(), description = "<:Coder_Hammer:826315685142462474> Ladies and gentlemen we got ||...||")
            em.add_field(name = 'Reason', value = 'I don\'t have the perms to do that-')
            em.add_field(name = 'What to do:', value = "Give me perms when?")
            em.set_footer(text = "-_-", icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Moderation(client))
