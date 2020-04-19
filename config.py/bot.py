import telebot
import config


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def echoe_func(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(content_types=['sticker'])
def sti_func(message):
    bot.send_sticker(message.chat.id, message.sticker.file_id)

@bot.message_handler(content_types=['audio'])
def audio_func(message):
    bot.send_audio(message.chat.id, message.audio.file_id)

@bot.message_handler(content_types=['photo'])
def ph_func(message):
   bot.send_photo(message.chat.id, message.photo[0].file_id) #Еле допер, что там был список O_o

@bot.message_handler(content_types=['document'])
def dcmt_dunc(message):
    bot.send_document(message.chat.id, message.document.file_id)

@bot.message_handler(content_types=['video'])
def vid_dunc(message):
    bot.send_video(message.chat.id, message.video.file_id)

@bot.message_handler(content_types=['voice'])
def voi_func(message):
    bot.send_voice(message.chat.id, message.voice.file_id)

bot.polling(none_stop=True)