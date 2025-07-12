import telebot

bot = telebot.TeleBot('7986029645:AAGO10LA6wXgnSQiG9-HPXvKZioPppN56Kc')
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,'Привет! Выбери чит на игру в Роблоксе.',)
@bot.message_handler(commands=['jailbreak'])
def main(message):
    bot.send_message(message.chat.id, 'ета чит на jailbreak перейди по силке')
bot.polling(none_stop=True)
