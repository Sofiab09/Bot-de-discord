import random as r, string as s, os
import asyncio, discord, yt_dlp as youtube_dl

# Configuración de yt-dlp
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0',
}

ffmpeg_options = {
    'options': '-vn',
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

def gen_pass(largo):
    elements = s.ascii_letters + s.digits + s.punctuation +s.ascii_lowercase +s.ascii_uppercase
    password =""

    for i in range(largo):
        password += r.choice(elements)

    return password

def flip_coin():
    flip = r.randint(0, 2)
    if flip == 0:
        return "CARA"
    else:
        return "SELLO"
    
# Clase para manejar el audio descargado
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            data = data['entries'][0]  # Si es una playlist, toma el primer elemento

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

def meme():
    with open ("img/meme 1.jpeg", "rb") as f:
        picture = discord.File(f)
    return picture

def memes():
    imgran = r.choice(os.listdir("img"))
    with open (f"img/{imgran}", "rb") as f:
        picture = discord.File(f)
    return picture

def motivacion():
    with open ("mot/motivacion 1.jpg","rb") as f:
        picture = discord.File(f)
    return picture