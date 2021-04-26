import discord

ID = 836044973778141254


def read_token():
    with open("K:\\Project\\Python\\MiracalDiscordBot\\token", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()

@client.event
async def on_member_join(member):
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(f"""Welcome to the server {member.mention}""")

@client.event
async def on_message(message):
    id = client.get_guild(ID)
    channels = ["commands"]

    if str(message.channel) in channels: # Check if in correct channel
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi")
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


client.run(token)
