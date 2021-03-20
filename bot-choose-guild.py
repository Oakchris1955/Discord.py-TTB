import discord

client = discord.Client()

channels_list = []
token = ''

@client.event
async def on_ready():
	print('Logged in(type)')
	while True:
		num = 1
		guild_list = []
		async for guild in client.fetch_guilds():
			print(num, '\t', guild.name)
			guild_list.append(guild.id)
			num+=1
		guild_number = int(input('Choose a guild: '))-1
		print(guild_list[guild_number])

		num = 1
		channels_list = client.get_guild(guild_list[guild_number]).text_channels
		for i in channels_list:
			print(num, '\t', i.name)
			num+=1
		channel_number = int(input('Choose a channel: '))-1
		print(channels_list[channel_number].name)
		channel = channels_list[channel_number]
		await channel.send(input('Enter your message here: '))
	    
#client.run(sys.argv[1:][0])
with open('token.txt') as tk:
	token = tk.read()
client.run(token)
