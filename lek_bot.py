import os
import random

import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Intents
intents = discord.Intents.default()
intents.message_content = True

# Initialize the Discord client with intents
client = discord.Client(intents=intents)


# Event handler for when the bot is ready
@client.event
async def on_ready():
    print('Bot is ready.')


# Event handler for when a message is received
@client.event
async def on_message(message):
    print(message)

    # Ignore messages sent by the bot itself to avoid infinite loops
    if message.author == client.user:
        return

    # Check if the message starts with the command prefix
    if message.content.startswith('!raffle'):
        await raffle(message)

async def raffle(message):
    message_split = str(message.content).split()

    # Handle list index out of range

    if not message_split[1].isnumeric():
        await message.channel.send("Please enter the number of winners")
        return

    number_of_winners = int(message_split[1])
    members = [member.removesuffix(",")for member in message_split[2:]]

    if len(members) == 0:
        await message.channel.send("Please enter members")
        return

    if number_of_winners >= len(members):
        await message.channel.send('Each member should receive at least ' + str(number_of_winners // len(members)))

    if number_of_winners % len(members) == 0:
        return

    random_selection = random.sample(members, number_of_winners % len(members))

    await message.channel.send('The winners are: ' + str(random_selection))


#!raffle 123 Gräslök/Ooocccooo, Bobby, Mubarak, Emil, styarn, Klurt, Benjamin/Vatten, schingo/ezbar, Synel, DavidFredrikAlbertThomson, Razzae, Borkii, Jompe/Xpwaste, Bibb-Urtid, GeneralSnoppi, viggo, Daim, Berra,


# Run the bot with its token
client.run(os.getenv('DISCORD_TOKEN'))