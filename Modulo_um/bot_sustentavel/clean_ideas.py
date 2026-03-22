import discord
from discord.ext import commands
import random
import os
import requests
import token

intents = discord.Intents.default()
intents.message_content = True

#Bot
but = commands.Bot(command_prefix='!', intents=intents)

artesanatos = {"papelão": "capa de livro",
               "papel": "caderno de anotações",
               "garrafa pet": "vaso de planta"}

random.choice(artesanatos)

#COMANDOS
@bot.event
async def on_ready():
    print(f'Logado como {bot.user} (ID: {bot.user.id})')

@bot.command('ajuda')
async def ajuda(ctx):
    message = ('Esse bot é capaz de compartilhar ideias de artesanatos que podem ser feitas com lixos recicláveis.')
    await ctx.send(message)

#Oferece ideias de artesanatos com lixo reciclável
@bot.command("artesanato")
async def artesanato(ctx,material: str):
    material = material.lower()
    await ctx.send(f'**{material.capitalize()}**{artesanatos[material]}')
    ideias = random.choice(artesanatos)
    print(ideias)
    

bot.run(token.TOKEN)