import requests
from telebot import types
import telebot
import base64
from bs4 import BeautifulSoup
import json
import random, string

import random, string

import os, time, sys
import requests,re,pyfiglet
O =  '\033[1;31m' #Red
Z =  '\033[1;37m' #white
F = '\033[1;32m' #Green
B = '\033[2;36m' #Light Blue
X = '\033[1;33m' #Yellow
C = '\033[2;35m' #Purpl
R = '\033[5;31m' #Red
logo = pyfiglet.figlet_format('CHAT GPT                                               BY')

print(R+logo)
logo2 = pyfiglet.figlet_format('OMER AKER')

print(B+logo2)
logo6 = ('your bot now online ')

print(O+logo6)

lo=(" ---------------------------------- ")

took =('7908671303:AAHhs-SmIYl1fxxiULETvmW-U4LI77E7T2w')
bot = telebot.TeleBot(took)
@bot.message_handler(commands=['start'])
def sd(message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("BY OMER AKER", url="https://t.me/omerislamaker")
    markup.add(btn)

    sd.sd = message.from_user.first_name
    bot.send_message(message.chat.id, f"أهلاً بك {sd.sd} في بوت الذكاء الاصطناعي. أرسل سؤالك للإجابة عليه.", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    saad = message.text
    a = message.from_user.first_name  
    Fix = saad 
    response = requests.get("https://ghostbin.site/csxio")
    LevIi = base64.b64decode(BeautifulSoup(response.text, 'html.parser').find('div', id='code').get_text(strip=True)).decode()

    url = "http://pass-gpt.nowtechai.com/api/v1/pass"
    payload = json.dumps({
        "contents": [
            {"role": "system", "content": LevIi},
            {"role": "user", "content": Fix}
        ]
    })

    headers = {
        'User-Agent': "Ktor client",
        'Connection': "Keep-Alive",
        'Accept': "application/json",
        'Accept-Encoding': "gzip",
        'Content-Type': "application/json",
        'Key': "OMER/l4RKTuqNDrIyUechJ0hp7d3z1zbe8o8eBrFlpMo0If/OMER+w==",
        'Accept-Charset': "UTF-8"
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        content_text = "".join(json.loads(line[5:])["content"] for line in response.text.splitlines() if '"status":"stream"' in line)
        bot.send_message(message.chat.id, content_text)
    except Exception as e:
        bot.send_message(message.chat.id, "حدث خطأ أثناء معالجة الطلب.")

bot.infinity_polling()
