import discord

client = discord.Client()

channels_list = []

@client.event
async def on_ready():
	while True:
		#inpmes = input('Enter: ')
		#print(bot.get_channel(817709050493403146))
		#channel = client.get_channel(817709050493403146)
		#await channel.send(input('Enter your message here: '))
		num = 1
		channels_list = client.get_guild(809490993770528808).text_channels
		for i in channels_list:
			global num
			print(num, '\t', i.name)
			num+=1
		channel_number = int(input('Choose a channel: '))-1
		print(channels_list[channel_number].name)
		channel = channels_list[channel_number]
		await channel.send(input('Enter your message here: '))
	    
client.run("your bot's token")
