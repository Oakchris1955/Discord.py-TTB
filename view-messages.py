import discord

client = discord.Client()
token = ''

@client.event
async def on_ready():
	print('Logged in (read)')

@client.event
async def on_message(message):
	print('In server:', message.guild, ', by:', message.author, ', Message:', message.content)

#client.run(sys.argv[1:][0])
#print(sys.argv[1:][0])
with open('token.txt') as tf:
	token = tf.read()
client.run(token)
