import telepot
import sys
import time
import subprocess
from pprint import pprint

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    #keyboard = InlineKeyboardMarkup(inline_keyboard=[
    #    [InlineKeyboardButton(text="cliccami", callback_data="press")]])
    if content_type == "text":
        if msg["text"] == "Spegni":
            bot.sendMessage(chat_id, "Ok, done")
            subprocess.run('shutdown -p', shell=True)
        if msg["text"] == "Sospendi":
            bot.sendMessage(chat_id, "Ok, done")
            subprocess.run('shutdown -f')

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor="callback_query")

bot = telepot.Bot("bot_api")
bot.message_loop({"chat": on_chat_message,
                  "callback_query": on_callback_query})

while True:
    time.sleep(1)
