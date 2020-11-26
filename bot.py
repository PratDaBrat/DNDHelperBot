#!/usr/bin/env python3

import os
import discord
from discord.utils import get
from dotenv import load_dotenv
#don't have the .env file idhar so this doesn't make a differnce neither does it run, discord doesn't let me share the token so
#when we work I'll give you the token and we'll regenerate it har baar

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
COMMAND = os.getenv('COMMAND')

client = discord.Client()

@client.event
async def on_ready():
	print('Bot is online')

@client.event
async def on_message(message):
	guild = message.channel.guild

	if message.author == client.user:
		return
	
	if client.user in message.mentions:
		if message.channel.guild.get_role(role) in message.author.roles: 
			user = message.author.display_name
			await message.channel.send(f'New session started by {user} in {guild}')
			SessionID = 1
			print(f'New session started: SessionID {SessionID}')
			await message.channel.send('Enter the name of the session moderator:')

		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

	if message.content.split(" ")[0] == '$mod':
		if message.channel.guild.get_role(role) in message.author.roles:
			mods = message.content.split(" ")[1:]
			session_roster['mods'] = mods
			await message.channel.send('Enter the name of the members of the government:')

		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

	if message.content.split(" ")[0] == '$gov':
		if message.channel.guild.get_role(role) in message.author.roles:
			gov = message.content.split(" ")[1:]
			session_roster['gov'] = gov
			await message.channel.send('Enter the name of the members of the opposition:')

		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

	if message.content.split(" ")[0] == '$opp':
		if message.channel.guild.get_role(role) in message.author.roles:
			opp = message.content.split(" ")[1:]
			session_roster['opp'] = opp
			await message.channel.send('Enter the name of the adjudiciators:')

		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

	if message.content.split(" ")[0] == '$adj':
		if message.channel.guild.get_role(role) in message.author.roles:
			adj = message.content.split(" ")[1:]
			session_roster['adj'] = adj
			''' text makes the output presentable '''
			text = ''
			for elem in list(session_roster):
				text += elem + ": "
				for mem in session_roster[elem]:
					l = session_roster[elem]
					if l[(len(l)-1)] != mem:
						text += mem + ', '
					else:
						text += mem + ''
				text += '\n'
			await message.channel.send(f'{text}')

		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

if message.content.split(" ")[0] == '$start':
		if message.channel.guild.get_role(ROLE) in message.author.roles:
			await guild.create_role(name='mod',color=discord.Colour(0xff6ec7),mentionable=True)
			await guild.create_role(name='gov',color=discord.Colour(0xffff00),mentionable=True)
			await guild.create_role(name='opp',color=discord.Colour(0xffff00),mentionable=True)
			await guild.create_role(name='adj',color=discord.Colour(0xffff00),mentionable=True)
			''' this adds the role '''
			for role in list(session_roster):
				roster = session_roster[role]
				role = get(guild.roles, name=role)
				for mem in roster:
					i = int(mem[3:21])
					for member in client.get_all_members():
						if member.id == i:
							await member.add_roles(role)
			 ''' end of block '''
		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

	if message.content.split(" ")[0] == '$stop':
		if message.channel.guild.get_role(ROLE) in message.author.roles:
			''' this block deletes the roles after session'''
			for role in list(session_roster):
				for r in guild.roles:
					if str(r) == role:
						await r.delete()
						print(role + " is deleted")
			''' end of block '''
		else:
			await message.channel.send(f'{user} is not authorised')
			await message.author.send("For instructions on how to use the bot contact a mod")

client.run(TOKEN)
