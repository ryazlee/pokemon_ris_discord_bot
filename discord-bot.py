import discord
import re
import requests
import string
import os

client = discord.Client()

regex_query = r'bulbagarden.net\/wiki\/Talk:([a-zA-Z]+)|bulbagarden.net\/wiki\/([a-zA-Z]+)|picuki.com\/tag\/([a-zA-Z]+)|pokemon.fandom.com\/wiki\/([a-zA-Z]+)|pokemondb.net\/pokedex\/([a-zA-Z]+)'

def query_url_creator(query):
    query = query.lower()
    if 'pokemon' not in query: 
        query += 'pokemon'
    return query.replace(string.whitespace, '+')

def search_pokemon_url(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    r = requests.get('http://www.google.com/searchbyimage?image_url=' + url, headers=headers)
    resp = re.findall(regex_query, r.text)
    flattened_resp = list(sum(resp, ()))
    return set(flattened_resp)

def search_pokemon_query(query):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    r = requests.get('http://www.google.com/search?q=' + query, headers=headers)
    resp = re.findall(regex_query, r.text)
    flattened_resp = list(sum(resp, ()))
    return set(flattened_resp)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('rb'):
        data = message.content.split('rb')
        potential_pokemon = search_pokemon_url(data[1]) if message.content.startswith('rbu') else search_pokemon_query(query_url_creator(data[1]))
        pp_str = ", ".join(str(p) for p in potential_pokemon if p)
        await message.channel.send("Potential pokemon: " + pp_str)
        print("query success: ", data[1])

client.run(os.environ.get('RB_PASSWORD'))
