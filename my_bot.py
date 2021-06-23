import discord
from discord import guild
from discord import message
from discord.ext import commands
import praw
import json
import os
import random
import asyncpraw


if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Prefix": "."}

    with open(os.getcwd() + "/config.json", "w+")  as f:
        json.dump(configTemplate, f)      





client = commands.Bot(command_prefix =".")

TOKEN = 'ODMxMjAxNTk4NTQ5MDAwMjcz.YHRy0A.KmHBETv_d6HUC5OA3OJC1EEj7cM'

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Welcome To Galactic ARK'))
    print('I Am Ready Boss')

#command

    @client.command()
    async def hi(ctx):
        
        await ctx.send('Hello!') 


    @client.command()
    async def who(ctx):
        
        await ctx.send('Your Friendly Neighborhood Galactic Ark') 

    @client.command()
    async def fire(ctx):
        
        await ctx.send(':flame:') 

    @client.command()
    async def bye(ctx):
        
        await ctx.send(':wave:') 


    @client.command()
    async def saste_nashe(ctx):
        
        await ctx.send('https://c.tenor.com/60lIZRxCGbsAAAAM/beerbiceps-ranveer-allahbadia.gif') 


    @client.command()
    async def yo(ctx):
        
        await ctx.send(':metal:') 


    @client.command()
    async def chapal(ctx):
        
        await ctx.send('https://tenor.com/view/gangs-of-wasseypur-mirzapur-indian-web-series-bhosdike-idhar-aa-gif-17086547') 



    @client.command()
    async def abe_saale(ctx):
        
        await ctx.send('https://tenor.com/view/abe-saale-sabbir31x-harmonium-sale-gif-15727715') 



    @client.command()
    async def storm_splits(ctx):
        
        await ctx.send('https://tenor.com/view/storm-splits-yt-gif-21005176') 


    @client.command()
    async def kon(ctx):
        
        await ctx.send('Don') 



    @client.command()
    async def dogo(ctx):
        
        await ctx.send('https://tenor.com/view/happy-dog-smiling-funny-animals-dogs-swing-gif-11733202') 


    @client.command()
    async def bruh(ctx):
        
        await ctx.send('https://tenor.com/view/touchdown-bruh-really-gif-12484222') 


    @client.command()
    async def itni_khushi(ctx):
        
        await ctx.send('https://tenor.com/view/itni-khushi-govinda-partner-happy-gif-17400523') 


    @client.command()
    async def hello(ctx):
        
        await ctx.send('Hello!') 

    @client.command()
    async def game_heaven(ctx):
        
         await ctx.send('https://tenor.com/view/gaming-heaven-game-07-007-gif-19771090') 


   # @client.command()
 #   async def dead_chat(ctx):
        
   #     await ctx.send('@here') 



    @client.command()
    async def tired(ctx):
        
        await ctx.send('https://tenor.com/view/anime-dazai-osamu-dazaiosamu-osamudazai-gif-8625630') 


    @client.command()
    async def cry(ctx):
        
        await ctx.send('https://tenor.com/view/milk-and-mocha-cry-sad-tears-upset-gif-11667710') 





    @client.command()
    async def bewafa(ctx):
        
        await ctx.send('https://tenor.com/view/bewafa-breakup-heartbreak-sad-crying-gif-18669103') 

    @client.command()
    async def gm(ctx):
        
        await ctx.send('https://tenor.com/view/cat-peek-a-boo-kitty-white-cat-cute-cat-gif-16415828')


    @client.command()
    async def namaste(ctx):
        
        await ctx.send('https://tenor.com/view/namaste-akshay-kumar-%E0%A4%A8%E0%A4%AE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%87-gif-11787886')




    @client.command()
    async def belinchi_nagin_nighali_hoye_hoye(ctx):
        
        await ctx.send('Muna o dola o lag laa')

    
    @client.command()
    async def gn(ctx):
        
        await ctx.send('https://tenor.com/view/night-good-night-sleep-tired-collapse-gif-10609182')

    
    @client.command()
    async def galactic_ARK(ctx):
        await ctx.send('https://tenor.com/view/galactic-ark-galactic-ark-gif-21408194')

    @client.command()
    async def sad(ctx):
        await ctx.send('https://tenor.com/view/peach-cat-guitar-playing-guitar-crying-tears-gif-17946924')


    @client.command()
    async def no_anime(ctx):
        await ctx.send("<:no_anime:853187081165471788>")

    @client.command()
    async def lol(ctx):
        await ctx.send("<a:LOLXD:852776819802636288>")


   
        
    



    @client.command()
    async def cool_boi(ctx):
        
        await ctx.send(':sunglasses:')

    @client.command()
    async def knock_knock(ctx):
        
        await ctx.send('Tera Bapp Aya')


@client.command()
async def av(ctx, *, user : discord.Member= None ):
    if user is None:
        user = ctx.message.author
    embed = discord.Embed()
    embed.add_field(name=user.name,value=f'[Download]({user.avatar_url})')   
    embed.set_image(url=user.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url= ctx.author.avatar_url)
    await ctx.send(embed=embed)





@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount+1)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Specify the number of messages to delete')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You dont have permission to do this')





client.remove_command("help")

@client.group(invoke_without_command=True)
async def help(ctx):
 em = discord.Embed(title = "Help", description = "Use .help <command> for extended information on a command ")


 em.add_field(name = "Fun", value = "|  `Text`  |  `Gif`  |  `Emoji`  |  `Meme`  |")
 await ctx.send(embed = em)
    

@help.command()
async def Text(ctx):

 em = discord.Embed(title = "Text",description = "**Send some funny text message**",color = ctx.author.color)
 em.add_field(name = "**commands**", value = "|  `hi` |  `who`  | `kon` | `hello` |  `knock_knock`  | `belinchi_nagin_nighali_hoye_hoye`  |")
 await ctx.send(embed = em)



@help.command()
async def Gif(ctx):

 em = discord.Embed(title = "Gif",description = "**Send a Gif related to message**",color = ctx.author.color)
 em.add_field(name = "**commands**", value = "|  `chapal` |  `abe_saale`  | `storm_splits`  | `dogo`  | `bruh`  | `itni_khushi`  | `tired`  | `cry` |  `bewafa` |  `gm` |  `gn` |  `saste_nashe` |  `namaste`  |  `galactic_ARK`  |  `game_heaven`  |  `sad`  |")
 await ctx.send(embed = em)


@help.command()
async def Emoji(ctx):

 em = discord.Embed(title = "Emoji",description = "**Send a Emoji related to message**",color = ctx.author.color)
 em.add_field(name = "**commands**", value = "|  `fire`  | `bye` |  `yo`  | `cool_boi`  |  `no_anime`  |  `lol`  |")
 await ctx.send(embed = em)


@help.command()
async def Meme(ctx):

 em = discord.Embed(title = "Meme",description = "**Send a Meme**",color = ctx.author.color)
 em.add_field(name = "**commands**", value = "|  `meme`  |")
 await ctx.send(embed = em)



#meme


reddit = asyncpraw.Reddit(client_id = "h-_O3UyqITE9zA",
                     client_secret = "X0xQVZ2K6KisYWMY42xZJrLIaWBtLw",
                     username = "Red_Flash55",
                     password = "rudransh55",
                     user_agent = "Galactic_ARK")


@client.command()
async def meme(ctx):
    subreddit = await reddit.subreddit("meme")
    all_subs = []
    top = subreddit.top(limit = 50)
    async for submission in subreddit.hot(limit=100):
     all_subs.append(submission)
    random_sub = random.choice(all_subs)
    name = random_sub.title
    url = random_sub.url
    em = discord.Embed(title = name)
    em.set_image(url = url)
    await ctx.send(embed= em)


@commands.has_permissions(manage_messages=True)
@client.command()
async def echo(ctx,*,msg):
  await ctx.message.delete()
  await ctx.send(msg)


@client.command()
async def say(ctx,*,msg):
    
  await ctx.send(msg)

#@client.event
#async def on_message(msg):

    #if ":" == message.content[0] and ":" == message.content[-1]:
        #emoji_name = message.content[1:-1]
        #for emoji in message.guild .emojis:
            #if emoji_name == emoji.name:
                #await message.channel.send(str(emoji))
               # await message.delete()
               # break
   # await client.process_commands(msg)        






client.run('ODMxMjAxNTk4NTQ5MDAwMjcz.YHRy0A.nv7ogJi4QQUyygP9-WOxLYeiabg')