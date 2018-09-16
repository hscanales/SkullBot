import discord
from discord.ext import commands


class Moderation:
	def __init__(self,bot):
		self.bot= bot

	@commands.command(pass_context=True)
	async def ban(self,ctx, *, member:discord.Member=None):
		if (member == self.bot.user ):
			await self.bot.say(ctx.message.author.mention + " No puedes banearme nub")
			await self.bot.delete_message(ctx.message)
		else:
			if (ctx.message.channel.permissions_for(ctx.message.author).ban_members):
				if (member == ctx.message.author):
					await self.bot.say(ctx.message.author.mention + " No puedes banearte a ti mismo")
					await self.bot.delete_message(ctx.message)
				else:
					await self.bot.say(ctx.message.author.mention + " Bans " + member.mention )
					await self.bot.ban(member)
					await self.bot.delete_message(ctx.message)
			else:
				await self.bot.say(ctx.message.author.mention + " No tienes permiso para usar este comando")
				await self.bot.delete_message(ctx.message)

	@commands.command(pass_context= True)
	async def kick(self,ctx,*,member:discord.Member=None):
		""" Kicks an user from the Guild/Server"""
		if(member==self.bot.user):
			await self.bot.say("@{} You can't kick me noob!".format(ctx.message.author))
			await self.bot.delete_message(ctx.message)
		else:
			if(ctx.message.channel.permissions_for(ctx.message.author).kick_members):
				if(member == ctx.message.author):
					await self.bot.say("@{} you can't kick yourself! ".format(ctx.message.author))	
					await self.bot.delete_message(ctx.message)
				else:
					await self.bot.say("Goodbye! "+ member.mention)
					await self.bot.kick(member)
			else:
				await self.bot.say("You don't have access to this command")

	@commands.command(pass_context=True)
	async def contact(self,ctx):
		embed = discord.Embed(title="Hello {}!".format(ctx.message.author), description="If you wish to contact the developers you can do: ", color=0x00ff00)
		embed.add_field(name="Instagram:", value="https://www.instagram.com/skullbot.py/ ", inline=True)
		embed.add_field(name="Discord Server:", value="https://dscrd.me/skullbotbeta", inline=True)
		embed.set_thumbnail(url="https://instagram.fsal1-1.fna.fbcdn.net/vp/f09a3e7ea448cc060bffb95e38cb74df/5B077F87/t51.2885-19/s150x150/27582150_1255412644592019_774178141550673920_n.jpg")
		await self.bot.say(embed=embed)

	@commands.command(pass_context=True)
	async def info(self,ctx,*,member:discord.Member=None):
		embed = discord.Embed(title="{}'s Info:".format(member.name),description="This is what i could find",color=0x00ff00)
		embed.add_field(title="Name: ",value=member.name, inline=True)
		embed.add_fiel(title="ID: ",value=member.id,inline=True)
		embed.add_field(title="Role: ", value=member.top_role)
		embed.add_field(title="Joined at: ",value=member.joined_at)
		embed.set_thumbnail(url=member.avatar_url)
		await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Moderation(bot))
    print('Moderation extension is Ready')