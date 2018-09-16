import discord
from discord.ext import commands
from discord.voice_client import VoiceClient
import logging
import random
import os


startup_extensions=["Music","Moderation"]
   
#Prefijo para llamar al bot desde Discord
command_prefix='!'
#definimos el bot
bot = commands.Bot(command_prefix)

#TOKENS
BETA="Mzk2NTU1MzE0MDEyMzU2NjE5.DSjIzw.ygHynfMgnYoaiqcliSqaF8TakhY"
#MAIN="Mzk2MTk3NDEwODE0MTY1MDAy.DSd-mA.pBRCF1IhhWhgkuIqQ0H3c9Ta-Y0"

@bot.event
async def on_ready():
    print("SkullBot Iniciando como:")
    print(bot.user.name)
    print(bot.user.id)
    print("----------------------")
    print("SkullBot Version 0.0.4-Release")
    await bot.change_presence(game=discord.Game(name="with BETA BOT|!help",type=0))
    


class Main_Commands():
    def __init__(self,bot):
        self.bot= bot

#aca el primer comando de prueba
@bot.command()
async def test(): #el nombre de la funcion es como se manda a llamar en discord, por ejemplo este se llamaria con $test
    """Testing if the bot is online or not """
    await bot.say(":computer: testing? Testing") #el async y el await no estoy muy seguro como funciona, pero si no lo pones no funciona :v




@bot.command(pass_context = True)
async def kill(ctx,*,member:discord.Member=None):
    """Kills and user from a a random  """
    #Diccionario de Homicidios
    kill={1:" asesino friamente usando una pala a ",2:" enveneno la comida de ", 3: " violo hasta matar a ", 4: " fue al pasado para darle pastillas de aborto a la madre de ",5: " le hizo tanto bullying a"}
    eleccion= kill[random.randrange(1,6)]
    await bot.say("Does not work for the moment, sorry ily <3 :smile:")
"""
    if (member == bot.user):
        await bot.say(ctx.message.author.mention + " Asi que estas intentando matarme? Preparate ")
        await bot.say(member.mention + eleccion + ctx.message.author.mention)
        await bot.delete_message(ctx.message)
    elif(member == ctx.message.author):
        await bot.delete_message(ctx.message)
        await bot.say(member.mention + " cometio suicidio porque es niño rata" )
    else:
        await bot.delete_message(ctx.message)
        await bot.say(ctx.message.author.mention + eleccion + member.mention)
"""





@bot.command()
async def ping():
    """:ping_pong: Pong! """
    await bot.say(":ping_pong:Pong!")




if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__,e)
            print('Failed to load extensions {}\n{}'.format(extension,exc))





bot.run(BETA) #aca se ejecuta el bot, lo que esta en el parentesis es el token.
