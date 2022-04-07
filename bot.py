from nextcord.ext import commands
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("TOKEN")
rand_api = os.getenv("RAND_API")

###########################################################################
# Bot code begins
###########################################################################

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
            rand_api)
        r = json.loads(response.text)
    except:
        print("ERROR: Could not retrieve joke")
        r = "Sorry, I couldn't think of a 'Chuck Norris' joke..."

    msg = f"```{r['joke']}```"
    await ctx.send(msg)


bot.run(bot_token)
