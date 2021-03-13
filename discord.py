import time

felcanje = True

print("Welcome to self bot!")
name = input("Input your username: ")
#name2 = input("Input your second username: ")

while felcanje == True:

    text = input(name + " Input: ")

    from discord_webhook import DiscordWebhook

    webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/819959647247138836/FGj_5c6VMj6B2dvrBWi6IOZn_aMSdUKbHO0fbdJf_ZA5tgvhbHt4QuMkufBcaF99m3Q9', content="**" + name + ": " + "**" + text)
    response = webhook.execute()

'''    time.sleep(0.5)

    text2 = input(name2 + " Input: ")

    from discord_webhook import DiscordWebhook

    webhook = DiscordWebhook(url='webhooklink', content="**" + name2 + ": " + "**" + text2)
    response = webhook.execute() '''
