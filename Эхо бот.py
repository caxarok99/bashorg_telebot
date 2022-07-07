import telebot
from telebot import types



@bot.message_handler(commands=['start',]) #При команде "Старт" бот здоровается.
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>' #Имя жирное, фамилия подчеркнута.
    bot.send_message(message.chat.id, mess, parse_mode="html") # бот отправляет приветствие в этот чат. Формат html.

#bot.message_handler(content_types=['text'])  Реакции бота на разные сообщения.
#ef get_user_text(message):
#    if message.text == 'Привет':
#       bot.send_message(message.chat.id, 'И тебе привет!', parse_mode="html")
#   elif message.text == 'Дурак':
#       bot.send_message(message.chat.id, 'Сама дура!', parse_mode="html")
#   elif message.text == 'photo':
#       photo=open('2.jpg', 'rb')
#       bot.send_photo(message.chat.id,photo  )
#   else:
#       bot.send_message(message.chat.id, 'Я Дубина и я тебя не понимаю', parse_mode="html")

@bot.message_handler(content_types=['photo']) #Реакция бота на отправку фоток
def get_user_photo(message):
    bot.send_message(message.chat.id,'Норм фотка')

@bot.message_handler(commands=['website']) #Команда 'вебсайт'.
def website(message):
    markup=types.InlineKeyboardMarkup() #Определяем тип кнопки, которая появится в сообщении.
    markup.add(types.InlineKeyboardButton('Сайт', url='https://yandex.ru')) #Добавляем в эту кнопку текст и ссылку.
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup) # Бот отправляет сообщение с кнопкой

@bot.message_handler(commands=['help']) #Команла хелп
def website(message):
    mar=types.ReplyKeyboardMarkup(resize_keyboard=True) #Переменная для типа кнопки, которая появится на клавиатуре телеги + адаптивный размер кнопок на клаве
    website=types.KeyboardButton('Веб сайт')  #Кнопка сайта. Всплывёт на клавиатуре
    start=types.KeyboardButton('Start') #Кнопка старт. Всплывёт на клавиатуре
    mar.add(website,start) #Добавляем эти кнопки в переменную.
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=mar) #Бот отправляет сообщение.


bot.polling(none_stop=True) #Бот запущен, работает без остановки



