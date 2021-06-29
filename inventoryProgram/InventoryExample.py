import os, discord, random, dotenv, selenium, asyncio, youtube_dl, ffmpeg, queue, datetime 
import time;

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

job_number = []
engaged = False

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)

@client.event
async def on_ready():    
    guilds = len(list(client.guilds))
    guild_list = '\n - '.join([guilds.name for guilds in client.guilds])
    print(client.user, 'is connected to', guilds, 'guilds:\n -', guild_list)


        

@client.command()
async def job(ctx, query):
    job_number.clear()
    try:
        content = query + '\n'
        with open('Job Numbers.txt') as f:
            if content in f.readlines():
                job_number.append(query)
                await ctx.send("What would you like to charge against " + query + "?")
            else:
                await ctx.send("Please enter a valid equipment/job number")
    except:
        await ctx.send("Please enter a valid equipment/job number")

        
@client.command()
async def signout(ctx, *query):
    count = len(job_number)
    try:
        if job_number != 0:
            member = ctx.author
            x = datetime.datetime.now()
            date_now = x.strftime("%b, %d")
            file_name = (date_now + ".txt")
            time_stamp = open(file_name, "a+")
            items = "{}".format(' '.join(query))
            time_stamp.write(str(member) + " signed out: " + items + " against " + job_number[0] + "\n")       
        else:
            await ctx.send("Please use !job before signing items out of lock-up.")
    except:
        await ctx.send("Please use !job before signing items out of lock-up.")

@client.command()
async def signin(ctx, *query):
    count = len(job_number)
    try:
        if job_number != 0:
            member = ctx.author
            x = datetime.datetime.now()
            date_now = x.strftime("%b, %d")
            file_name = (date_now + ".txt")
            time_stamp = open(file_name, "a+")
            items = "{}".format(' '.join(query))
            time_stamp.write(str(member) + " put back: " + items + " against " + job_number[0] + ".\n")       
        else:
            await ctx.send("Please use !job before signing items in to lock-up.")
    except:
        await ctx.send("Please use !job before signing items in to lock-up.")


client.run(TOKEN)
