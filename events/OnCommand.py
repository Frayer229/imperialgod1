import discord
from discord.ext import commands
import random
import aiosqlite

class OnCommand(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Command events is ready!')

    @commands.Cog.listener()
    async def on_command(self, ctx):
        res = random.randint(1, 100)
        earnings = random.randint(2, 1000)
        tips = [
            '**Tip:** You can vote for 15,000 :coin: in the economy system!\n**Vote:** https://top.gg/bot/768695035092271124/vote/\n\nOnce you vote you should type `imp rewards vote`.',
            '**Tip:** You can join our support for any issues: https://discord.gg/dxF3EjVz',
            '**Tip:** You can try out our economy system by `imp help economy`',
            '**Tip:** Did you know I have a music system, try doing this with: `imp join`.\nAnd then play your favorite song: `imp play <songURL>`',
            '**Tip:** Did you know I am **100% open source: https://github.com/NightZan999/TheImperialGod**',
            '**Tip:** Did you know about my wesbite: **https://www.theimperialgod.ml/**'
        ]
        if res > 75:
            async with aiosqlite.connect("./data/economy.db") as connection:
                async with connection.cursor() as cursor:
                    await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                    rows = await cursor.fetchone()
                    if not rows:
                        await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                        await connection.commit()

                    if earnings > 700:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))

            await ctx.send(random.choice(tips))
            
            if earnings > 700:
                em = discord.Embed(title = "holy palpatine...", color = discord.Color.random(), description = f"You got **damn lucky from using the `{ctx.command.name}` command**!\nYou found **{earnings}** coins! Contact the developer if you'd like to say a big fat thanks to him (<@575706831192719370>)")
                em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
                em.set_thumbnail(url = ctx.guild.icon_url)
                await ctx.send(embed = em)

def setup(client):
    client.add_cog(OnCommand(client))