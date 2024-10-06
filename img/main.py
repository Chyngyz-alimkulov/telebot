import telebot
import random

API_TOKEN = "6423366069:AAGsQMb-u7-NKrcZKWo_Jh5cEPA9DVgh1e8"

bot = telebot.TeleBot(API_TOKEN, parse_mode="HTML")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'ПРИВЕТ СИГМА')

@bot.message_handler(commands=['kibub'])
def send_random_image(message):
    try:
        random_index = random.randint(0, 3)
        image_path = f"./img/image{random_index}.jpg"

        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка {e}")

@bot.message_handler()
def send_welcome(message):
    response = "<b>ТЫ ЧО ПИШЕШЬ НУБ Я ТЕБЯ НЕ ПОНИМАЮ</b>"
    bot.reply_to(message, response)

bot.polling()

    