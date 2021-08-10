#Using Flask as web servers
from flask import Flask
#Runs on separate thread from the bot
from threading import Thread

app = Flask('')

@app.route('/')
def home():
  return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()