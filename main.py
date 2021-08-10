import os
import discord
import requests
import json
from keep_alive import keep_alive
from Script import link_maker


# Connection to discord
client = discord.Client()   


def get_lowest_price(item_name):
  #use http api to get info online and data is stored in JSON
  response = requests.get(link_maker.setlink(item_name))
  #That's why we import json lib
  json_data = json.loads(response.text)
  quote = json_data['lowest_price']
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

  # gives lowest price of the desire item
  if msg.startswith('$find'):
    #Take the user input and split the message
    #For the method we required second element which is item's name
    item_name = msg.split("$find ", 1)[1]
    # Calls the function from above
    lowest_price = get_lowest_price(item_name)
    await message.channel.send("My Guy! {} is {}".format(item_name, lowest_price))


#keep the bot online all the time
keep_alive()


# This how you run the bot
# token (using replit feature)
my_secret = os.environ['TOKEN'] 
client.run(my_secret) 