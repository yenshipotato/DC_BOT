import discord
import keep_alive
import spider
from discord.ext import commands

bot = commands.Bot(command_prefix="")

@bot.event
async def on_ready():
    print("BOT is Online")

@bot.event
async def on_message(message):
    if message.content == "H":
        emb = discord.Embed()
        emb.set_image(url = "https://i.stack.imgur.com/LDUmI.png")
        await message.channel.send(content = None,embed = emb)
    print(message.content)
    
    target = spider.search(message.content)
    if target !="NOT FOUND" and message.author.nick!="TEST_LOL":
        img = spider.web_crawl(target)
        for text in img:
            await message.channel.send(content=text)
    

bot.run("token")
keep_alive.keep_alive()
