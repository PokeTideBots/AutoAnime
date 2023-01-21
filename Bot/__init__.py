import logging 
from os import environ, path, remove
from sys import exit
from pyrogram import Client 
from pyromod import listen

if path.exists('log.txt'):
    remove('log.txt')
    
logging.basicConfig(filename='log.txt', level=logging.INFO)
LOG = logging.getLogger("AutoPahe")
LOG.setLevel(level=logging.INFO)

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}

API_ID = int(environ.get('API_ID', 4783634)) #API ID
API_HASH = environ.get('API_HASH', "f6c33f46599246676f75e153b615dbbc") #API HASH
BOT_TOKEN = environ.get('BOT_TOKEN', "5872952946:AAHVZRDj2wIY_KWjAWbXfM2vAp5lOmRcAsQ") #BOT TOKEN
DATABASE_URL = environ.get('DATABASE_URL', "mongodb+srv://Devilharsha:Devilharsha@cluster0.exwkd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority") #MONGO DB
OWNER_ID = int(environ.get('OWNER_ID', 1165699179)) #OWNER ID
MAIN_CHANNEL = int(environ.get('MAIN_CHANNEL', -1001763302512))#YOUR MAIN CHANNEL ID
ARCHIVE_CHANNEL = int(environ.get('ARCHIVE_CHANNEL', -1001645644921))#YOUR ARCHIVE CHANNEL
MESSAGE_ID = int(environ.get('MESSAGE_ID', 76)) #SUB CHANNEL STATUS ID

soheru = Client('SoheruBots', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins=dict(root="Bot/plugins"))
