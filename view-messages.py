import discord

client = discord.Client()
token = ''

@client.event
async def on_ready():
	print('Logged in (read)')

@client.event
async def on_message(message):
	print('From:',message.author,', In:',message.guild,', Channel:',message.channel,', Content:',message.content)

with open('token.txt') as tf:
	token = tf.read()
client.run(token)
