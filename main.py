import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import logging
import random
import os
import smtplib



donors="donadores.txt"
donadores=[]

def borrar():
    del donadores[:]

def cargar():
    file=open(donors,"r")
    for line in file:
        donadores.append(line.strip("\n"))



startup_extensions=["Music","Moderation"]
   
#Prefijo para llamar al bot desde Discord
command_prefix='$'
#definimos el bot
bot = commands.Bot(command_prefix)
#TOKENS
BETA="placeholder"

@bot.event
async def on_ready():
    print("SkullBot Iniciando como:")
    print(bot.user.name)
    print(bot.user.id)
    print("----------------------")
    print("SkullBot Version 0.0.4-Release")
    cargar()
    await bot.change_presence(game=discord.Game(name="with SkullBot|$help",type=0))





class Main_Commands():
    def __init__(self,bot):
        self.bot= bot

#aca el primer comando de prueba
@bot.command()
async def test(): #el nombre de la funcion es como se manda a llamar en discord, por ejemplo este se llamaria con $test
    """Testing if the bot is online or not """
    await bot.say(":computer: testing? Testing") #el async y el await no estoy muy seguro como funciona, pero si no lo pones no funciona :v

@bot.command(pass_context=True)
async def vip(ctx):
    """If you are a Donor and need help, do this """
    if ctx.message.author.id in donadores:
        await bot.send_message(ctx.message.author,"Join SkullBot Beta Server to talk to the developers if you have anyproblem")
        await bot.send_message(ctx.message.author,"https://dscrd.me/skullbotbeta")
    else:
        await bot.send_message(ctx.message.author,"You are not a donor, if you want to donate send a message to our instagram (use $contact)")

@bot.command()
async def ping():
    """:ping_pong: Pong! """
    await bot.say(":ping_pong:Pong!")

@bot.command(pass_context=True)
async def update(ctx):
    """Dev Only Command """
    if (ctx.message.author.id == "411624416213204992" ) or (ctx.message.author.id=="181125952032473088") or (ctx.message.author.id == "396402061572440067"):
        borrar()
        cargar()
        await bot.send_message(await bot.get_user_info(181125952032473088),"Base de Datos de Donadores Actualizada")
        print(donadores)
    else:
        await bot.send_message(ctx.message.author,"You dont have access to this function '$vip' ")


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('Failed to load extensions {}\n{}'.format(extension,exc))





bot.run(BETA) #aca se ejecuta el bot, lo que esta en el parentesis es el token.
