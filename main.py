import discord
import logging


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# @client.event
# async def on_raw_reaction_add(payload):
#     payload.channel.send(payload.emoji)

client.run('Nzg4MjkzOTExNDc4NjY1MjI2.X9hZ6g.ye_zhiJLoA1RlewrHg81BfDs84k')