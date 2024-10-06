from telebot import types, TeleBot


API_TOKEN = '6423366069:AAGsQMb-u7-NKrcZKWo_Jh5cEPA9DVgh1e8'

bot = TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("СИГМА", callback_data="btn1")
    btn2 = types.InlineKeyboardButton("ЗАРЕГЕСТРИРОВАТЬСЯ НА ТУРНИР", url="https://t.me/sigma_chadic")

    keyboard.row(btn1)
    keyboard.row(btn2)
    
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

#     btn_yes = types.KeyboardButton("КАКАТЬ!")
#     btn_no = types.KeyboardButton("ПУКАТЬ!")

#     keyboard.add(btn_yes, btn_no)

    bot.send_message(message.chat.id, "<b>ПРИВЕТ, ЭТО ТУРНИРЫ ПО БРАВЛ СТАРСУ ОТ ЧЫНГЫЗА!</b>", reply_markup=keyboard)

@bot.message_handler(countent_types=["photo"])
def send_photo(message):
    bot.reply_to(message, "Great photo")

# @bot.message_handler()
# def any_message(message):
#     if message.text == "КАКАТЬ!":
#         bot.send_message(message.chat.id, "<i>ТОЛЬКО НЕ ОБКАКАЙСЯ ЗДЕСЬ, СОСУНОК</i>")
#     elif message.text == "ПУКАТЬ!":
#         bot.reply_to(message, "НУ ТОГДА МОЖЕШЬ ПУКАТЬ, ТОЛЬКО ЧТОБ НЕ ВОНЯЛО")

bot.polling()
