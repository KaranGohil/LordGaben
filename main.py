import os
import discord
import requests
import json
from keep_alive import keep_alive


# Connection to discord
client = discord.Client()   


def get_quote():
  #use http api to get info online and data is stored in JSON
  response = requests.get("http://steamcommunity.com/market/priceoverview/?appid=730&currency=20&market_hash_name=Snakebite Case")
  #That's why we import json lib
  json_data = json.loads(response.text)
  print(json_data)
  # the first part will return the quote and second the author's name
  #'q' and 'a' are key name and return value
  quote = json_data['volume'] + " -"+ json_data['lowest_price']
  return(quote)


#asynchronous lib, works on event and callback
@client.event
async def on_ready():
  #String method format - 0 is replace by client
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  #If the message is from client(ourselves), return it
  if message.author == client.user:
    return 

  #improvement as we are going to use message.content alot
  #this variable stores user's response
  msg = message.content 

  #command to operate the bot (set here)
  if msg.startswith('$hello'):
    #command to show/send the message on discord (channel)
    await message.channel.send('Hello!')

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)



#keep the bot online all the time
keep_alive()


# This how you run the bot
# token (using replit feature)
my_secret = os.environ['TOKEN'] 
client.run(my_secret) 