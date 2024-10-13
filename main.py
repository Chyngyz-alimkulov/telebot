from telebot import types, TeleBot

API_TOKEN = '6423366069:AAGsQMb-u7-NKrcZKWo_Jh5cEPA9DVgh1e8'

bot = TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    btn1 = types.KeyboardButton("🤚")
    btn2 = types.KeyboardButton("✊")
    btn3 = types.KeyboardButton("✌️")
    
    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
   
    bot.send_message(message.chat.id, "<b>ПРИВЕТ, ЭТО БОТ КАМЕНЬ НОЖНИЦЫ БУМАГА!</b>", reply_markup=keyboard)

@bot.message_handler()
def any_message(message):
    random.choice(['✊', '🤚', '✌️'])
    if message.text == "✌️":
        bot.send_message(message.chat.id, "<i>✊ Ты проиграл</i>")
    elif message.text == "🤚":
        bot.reply_to(message, "🤚 Ничья")
    elif message.text == "✊":
        bot.reply_to(message, "✌️ Ты выйграл")
        
bot.polling()