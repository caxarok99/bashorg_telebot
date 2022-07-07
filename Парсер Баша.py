import requests
from bs4 import BeautifulSoup as b
import random
import telebot

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.160 YaBrowser/22.5.2.615 Yowser/2.5 Safari/537.36"
}

URL='http://bashorg.org/page/'

def quote(url):
    global page
    r = requests.get(f'{url}{page}')
    page += 1
    html=b(r.text,'html.parser')
    citt=html.find_all('div', class_='quote')
    return [c.text for c in citt]
page=1
quotes = quote(URL)
bot = telebot.TeleBot('5444332840:AAEo66nGVjKVwfQ9FDxYRugBD5Rn5W5mwec')
random.shuffle(quotes)

@bot.message_handler(content_types=['text'])

def cit(message):
    quotes = quote(URL)
    if message.text.lower() in ('123456789'):
        bot.send_message(message.chat.id, (quotes[0]))
        del quotes[0]
        if len(quotes) == 0:
            quotes=quote(URL)
    else:
        bot.send_message(message.chat.id, 'Введи любую цифру ДО 9')


bot.polling(none_stop=True)








