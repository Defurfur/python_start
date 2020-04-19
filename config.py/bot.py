import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def echoe_func(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)


bot.polling(none_stop=True)
