#libraries
import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#when a member joins a server
@client.event
async def on_member_join(member):
    #send message in the general channel
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(
                f'Welcome to the server {member.mention}'
            )
    
    #send a dm
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

#when a member leaves the server
@client.event
async def on_member_remove(member):
    print(f'{member.name} has left the server!')

    #send a message in general channel
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send_message(
                f'{member.mention} has left the server'
            )


#event when user types out '!hello' or 'hi'
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.find("!hello") or message.content.find("!hi"):
        await message.channel.send(f'Hi!')

client.run("your-bot-token")