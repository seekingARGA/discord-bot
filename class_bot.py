# test-bot(bot class)

import discord
import random
from discord.ext import commands
from bot_logic import gen_pass
import os
import requests

description = "Contoh bot Discord dengan berbagai fitur."

# Bot intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot instance (with custom help)
bot = commands.Bot(command_prefix='$', description=description, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

# Math Commands
@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def min(ctx, left: int, right: int):
    await ctx.send(left - right)

@bot.command()
async def times(ctx, left: int, right: int):
    await ctx.send(left * right)

@bot.command()
async def divide(ctx, left: int, right: int):
    await ctx.send(left / right)

@bot.command()
async def exp(ctx, left: int, right: int):
    await ctx.send(left ** right)

# Meme Command
@bot.command()
async def meme(ctx):
    with open('meme/meme1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

# Dog and Duck API
def get_dog_image_url():
    res = requests.get('https://random.dog/woof.json')
    return res.json()['url']

@bot.command()
async def dog(ctx):
    await ctx.send(get_dog_image_url())

def get_duck_image_url():
    res = requests.get('https://random-d.uk/api/random')
    return res.json()['url']

@bot.command()
async def duck(ctx):
    await ctx.send(get_duck_image_url())

# File Writing
@bot.command()
async def tulis(ctx, *, my_string: str):
    with open('kalimat.txt', 'w', encoding='utf-8') as t:
        t.write(my_string)

@bot.command()
async def tambahkan(ctx, *, my_string: str):
    with open('kalimat.txt', 'a', encoding='utf-8') as t:
        t.write('\n' + my_string)

@bot.command()
async def baca(ctx):
    with open('kalimat.txt', 'r', encoding='utf-8') as t:
        await ctx.send(t.read())

# Repeat Message
@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    for _ in range(times):
        await ctx.send(content)

# Password Generator
@bot.command()
async def pw(ctx):
    await ctx.send(f'Kata sandi yang dihasilkan: {gen_pass(10)}')

@bot.command()
async def animal(ctx):
    with open('meme/animalmeme.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def bye(ctx):
    await ctx.send('🙂')

# Coinflip
@bot.command()
async def coinflip(ctx):
    await ctx.send('It is Head!' if random.randint(1, 2) == 1 else 'It is Tail!')

# Dice
@bot.command()
async def dice(ctx):
    await ctx.send(f'It is {random.randint(1, 6)}!')

# Member Joined Info
@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

# Local File Viewer
@bot.command()
async def local_drive(ctx):
    try:
        files = os.listdir("./files")
        file_list = "\n".join(files)
        await ctx.send(f"Files in the files folder:\n{file_list}")
    except FileNotFoundError:
        await ctx.send("Folder not found.")

@bot.command()
async def showfile(ctx, filename):
    file_path = os.path.join("./files", filename)
    try:
        await ctx.send(file=discord.File(file_path))
    except FileNotFoundError:
        await ctx.send(f"File '{filename}' not found.")

@bot.command()
async def simpan(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            await attachment.save(f"./files/{attachment.filename}")
            await ctx.send(f"Menyimpan {attachment.filename}")
    else:
        await ctx.send("Anda lupa mengunggah :(")

@bot.command()
async def help(ctx):
    help_message = """
i gotchu:
add [a] [b]         → tambah dua angka
min [a] [b]         → kurangi dua angka
times [a] [b]       → kali dua angka
divide [a] [b]      → bagi dua angka
exp [a] [b]         → pangkat
dog                 → kirim gambar anjing acak
duck                → kirim gambar bebek acak
meme                → kirim meme lokal
repeat [n] [msg]    → ulangi pesan n kali
dice                → lempar dadu
coinflip            → lempar koin
pw                  → buat password acak
tulis [teks]        → tlis ke file
tambahkan [teks]    → tambah ke file
baca                → baca isi file
local_drive         → lihat file lokal
showfile [nama]     → tampilkan file lokal
simpan              → simpan file dari attachment
joined [@user]      → lihat kapan user bergabung
bye                 → kirim salam
"""
    await ctx.send(help_message)

# Run the bot
bot.run('token!!!!!')

