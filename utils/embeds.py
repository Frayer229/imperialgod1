import discord

async def createEmbed(title, desc = None, footer = None, thumbnail = None):
    if desc is not None:
        em = discord.Embed(title = title, description = desc)
    else:
        em = discord.Embed(title = title)
    if footer is None:
        em.set_footer(text = "Bot made by NightZan999#0194")
    else:
        em.set_footer(text = footer)
    if thumnail is not None:
        em.set_thumbnail(url = thumnail)
    return em