import requests
import datetime
import telebot
from telebot.types import Message


TOKEN = "611944453:AAF2MVI5oEAle9i4yXs3qy9SMmmlpO1Jk4E"
STICKER_ID_1 = "CAADAgADFQADPwy8FAc8vAe6BKBLAg"



bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help','time'])

def start_handler(message: Message):
    now = datetime.datetime.now()
    if 'time' in message.text:
        msg = bot.send_message
        now_time = str(str(now.hour)+ ':' + str(now.minute) + ':' + str(now.second))
        msg(message.chat.id, text= str('Now time:   ' +  str(now_time )+ '\nWrite /endless for check the end lessons'))

    if 'start' in message.text:
        msg = bot.send_message
        msg(message.chat.id, text=str('Hello, my name Steve. I bot, I can write time which remains until the end lessons. '
                                      'Write /endless'))
    if 'help' in message.text:
        msg=bot.send_message
        msg(message.chat.id, text= str( 'Right /time or /endless '))




                                        #Text Bot
@bot.message_handler(content_types=['text'])
@bot.edited_message_handler(content_types=['text'])
def echo_digits(message: Message):
    msg = bot.send_message
    mci = message.chat.id
    mt = message.text
    if 'About Taras' in mt:
        msg(mci, text = '18.y.o live in Brovary city.')

    if 'ty' in mt:
        msg(mci, text = 'No problem')
        return



                        #Sticer
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    bot.send_sticker(message.chat.id,STICKER_ID_1)
bot.polling()