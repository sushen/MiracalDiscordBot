import discord


def read_token():
    with open("K:\\Project\\Python\\MiracalDiscordBot\\token", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.find("hello") != -1:
        await message.channel.send("hi")



client.run(token)
