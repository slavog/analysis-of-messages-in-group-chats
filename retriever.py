import configparser
import json

from telethon.sync import TelegramClient
from telethon import connection

# for correct transfer the time of messages to json
from datetime import date, datetime

# classes for working with channels
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# class for working with messages
from telethon.tl.functions.messages import GetHistoryRequest

# reading user data
config = configparser.ConfigParser()
config.read("configs.ini")

# assign a value to a variable
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']

# Telegram authorization
client = TelegramClient(username, int(api_id), api_hash)
client.start()
