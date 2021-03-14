import discord

client = discord.Client()

@client.event
async def on_message(message):
	print('In server:', message.guild, ', by:', message.author, ', Message:', message.content)

client.run("Enter your bot's token here") #change this string ⏪
