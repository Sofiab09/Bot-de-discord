import discord, os, logic as l
from dotenv import load_dotenv
from discord.ext import commands
from commandAPI import * 
from Ambiente import *

load_dotenv()
token = os.getenv("dt")

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name="contraseña")
async def password (ctx, lenght = 25):
    x = l.gen_pass(lenght)
    await ctx.send(f"🔐su contraseña ha sido generada: {x}")

@bot.command(name = "moneda")
async def coin(ctx):
    x = l.flip_coin()
    await ctx.send(f"📀El resultado fue: {x}")
    
# Comando: Reproducir música desde YouTube
@bot.command(name="yt")
async def yt(ctx, *, url):
    if not ctx.voice_client:
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
        else:
            await ctx.send("❌ ¡Debes estar en un canal de voz para usar este comando!")
            return

    async with ctx.typing():
        player = await l.YTDLSource.from_url(url, loop=bot.loop)
        ctx.voice_client.play(player, after=lambda e: print(f"Error: {e}") if e else None)

    await ctx.send(f"🎶 Reproduciendo ahora: **{player.title}**")

@bot.command(name="meme")
async def memes(ctx):
    f = l.meme()
    await ctx.send(file = f)

@bot.command(name="memes")
async def momo(ctx):
    f = l.memes()
    await ctx.send(file = f)

@bot.command(name="motivame")
async def motivame(ctx):
    f = l.motivacion()
    await ctx.send(file = f)

@bot.command(name="patos")
async def pato(ctx):
    img_pato = duck_image()
    await ctx.send(img_pato)

@bot.command(name="anime")
async def animes(ctx, x):
    query = x
    img_anime = anime_poster(query)

    if img_anime: 
        for anime in img_anime:
            img_url= anime["attributes"]["posterImage"]["small"]
            await ctx.send(f"urlimage:{img_url}")
    
    else:
        await ctx.send("No se pudo encontrar")


@bot.command(name="eco")
async def animes(ctx, opcion:int):
    if opcion == 1:
        await ctx.send(embed=etiqueta_reducción())

    elif opcion == 2:
        await ctx.send(embed=etiqueta_reutilizarReciclar())

    elif opcion == 3:
        await ctx.send(embed=etiqueta_consumoResponsable())

    else:
        await ctx.send("Opción Invalida, elija 1,2 o 3")



bot.run(token)


