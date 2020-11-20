import discord
import time

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

    if message.channel.name == 'pokemon':
        for i in range(20):
            await message.channel.send("this is text for poketwo")
            time.sleep(3)


client.run('Nzc5NDg1OTI5MzQ0OTkxMjU0.X7hO1w.dFiQ_kqL4_qGqFp-kpo_AasdMBs')
