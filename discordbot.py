import discord, os, logic as l
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("dt")

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")

    elif message.content.startswith("Contra"):
        ctr = l.gen_pass(25)
        await message.channel.send(f"Su contraseña es: {ctr}")
        
    elif message.content.startswith("Coin"):
        Moneda = l.flip_coin()
        await message.channel.send(f"El resultado fue: {Moneda}")
    else:
        await message.channel.send(message.content)

client.run(token)
