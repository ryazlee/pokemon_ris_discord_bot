import discord
import time
from bs4 import BeautifulSoup
import re
import requests

client = discord.Client()

def search_pokemon(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    r = requests.get('http://www.google.com/searchbyimage?image_url=' + url, headers=headers)
    resp = re.findall(r'wiki\/([a-zA-Z]+)|pokemon\+(\w+)|picuki.com\/tag\/(\w+)|gramho.com\/explore-hashtag\/(\w+)', r.text)
    flattened_resp = list(sum(resp, ()))
    return set(flattened_resp)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rb'):
        data = message.content.split()
        potential_pokemon = search_pokemon(data[1])
        pp_str = ", ".join(str(p) for p in potential_pokemon if p)
        await message.channel.send("Potential pokemon: " + pp_str)

client.run('Nzc5NDg1OTI5MzQ0OTkxMjU0.X7hO1w.dFiQ_kqL4_qGqFp-kpo_AasdMBs')
