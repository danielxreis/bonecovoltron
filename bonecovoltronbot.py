import os
import random
import discord
import re

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

cliente = discord.Client()

@cliente.event
async def on_ready():
    print(f'{cliente.user} está conectado no GTZcord')

@cliente.event
async def on_message(mensagem):
    if mensagem.author == cliente.user:
        return
    temaotil = re.search("(ão)$", mensagem.content)
    print(temaotil)
    if temaotil:
        frase = "meu pau na sua mão"
        await mensagem.channel.send(frase)

cliente.run(TOKEN)