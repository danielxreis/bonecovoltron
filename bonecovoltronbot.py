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

# Regra 1: Identifica se alguém escrever alguma frase que finalize com "ão" para enviar a resposta adequada.
@cliente.event
async def on_message(mensagem):
    # Verifica se não é o Bot quem está enviando a mensagem
    if mensagem.author == cliente.user:
        return
    # Verifica se a condição foi "não", caso tenha sido, não faça nada.
    regexNao = "(não)$|(não)[!?. ]$"
    nao = re.search(regexNao, mensagem.content)
    if nao is None:
        regex = "(ão)$|(ão)[!?. ]$"
        teste = re.search(regex, mensagem.content)
        if teste:
            await mensagem.channel.send("meu pau na sua mão", tts=True)

cliente.run(TOKEN)