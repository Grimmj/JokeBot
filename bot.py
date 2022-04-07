import discord
from nextcord.ext import commands
import requests
import os
import json

# Client code
# client = discord.Client()

# @client.event
# async def on_ready():
#     print("We have logged in as {0.user}".format(client))

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if message.content.startswith("$hello"):
#         await message.channel.send("Hello!")

# client.run("OTI0ODI4NzM3MjE4OTUzMjI3.YckP4Q.kCrcVbOxe4iwVyfk-OGsPv9XklI")

# Bot code

bot = commands.Bot(command_prefix="$", description="This is a Helper Bot")

bot.remove_command('help')


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def help(ctx):
    await ctx.send(
        "```I am JokeBot. I can only do four things.\nHere is a list of my commands:\n $help \n $dad \n $yomomma \n $chuck \n $random```"
    )


@bot.command()
async def dad(ctx):
    try:
        response = requests.get(
            "https://icanhazdadjoke.com/", headers={"Accept": "text/plain"}
        )
    except:
        print("ERROR: Could not retrieve joke")
        response = "Sorry, I couldn't think of a dad joke..."

    msg = f"```{response.text}```"
    await ctx.send(msg)


@bot.command()
async def yomomma(ctx):
    try:
        response = requests.get("https://api.yomomma.info/")
        r = json.loads(response.text)
    except:
        print("ERROR: Could not retrieve joke")
        r = "Sorry, I couldn't think of a 'Yo Momma' joke..."

    msg = f"```{r['joke']}```"
    await ctx.send(msg)


@bot.command()
async def chuck(ctx):
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        r = json.loads(response.text)
    except:
        print("ERROR: Could not retrieve joke")
        r = "Sorry, I couldn't think of a 'Chuck Norris' joke..."

    msg = f"```{r['value']}```"
    await ctx.send(msg)


@bot.command()
async def random(ctx):
    try:
        response = requests.get(
            "https://v2.jokeapi.dev/joke/Miscellaneous,Dark,Pun?blacklistFlags=racist,sexist,explicit&type=single")
        r = json.loads(response.text)
    except:
        print("ERROR: Could not retrieve joke")
        r = "Sorry, I couldn't think of a 'Chuck Norris' joke..."

    msg = f"```{r['joke']}```"
    await ctx.send(msg)


bot.run("[TOKEN HERE]")
