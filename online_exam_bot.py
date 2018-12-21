#-*. coding: utf:8 -*-
import sys
import time
import datetime
import telepot
import requests
import pymongo
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup,InlineKeyboardButton
from pprint import pprint
import numpy
import matplotlib.pyplot
import xlsxwriter
import pandas

# Token gotten from telegram botfather

Token = '722321256:AAHZYQTTVlopUXAuTQTIHVvjKa5iIbLZ5fQ'

# Welcome Message

welcome_message = 'خوش آمدید'

#the command for creating the bot based on the Token that bot father gave us

bot = telepot.Bot(Token)

#to understand that bot is working correctly

print(bot.getMe(),'\n')
print('Listening...\n')
