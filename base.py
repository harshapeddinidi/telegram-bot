# -*- coding: utf-8 -*-

import check
from telegram.ext import Updater,CommandHandler,MessageHandler, Filters
import os
Token="376593798:AAHMNABESGpXiFGiQ8Bg-0CnHc2EwyXD1hk"
updater = Updater(token=Token)
dispatcher = updater.dispatcher

def start(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Bot çalışıyor.")
def hello(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id,text="Hello "+update.message.from_user.first_name)
def echo(bot,update):
    bot.sendMessage(chat_id=update.message.chat_id,text="Merhaba "+update.message.from_user.first_name)
    bot.sendMessage(chat_id=update.message.chat_id, text="Kaynak atmak için /kaynak <link>")
    bot.sendMessage(chat_id=update.message.chat_id,text="Bota Hello dedirtmek için /hello")

def kaynak(bot,update):

    msg = update.message.text
    x = str(msg ).replace("/kaynak"," ")
    k =  x.split(" ")
    a=check.url(k[2])
    print(x)
    if (a == True):
        bot.sendMessage(chat_id=update.message.chat_id, text=update.message.from_user.first_name +
                                                             "'nin Kaynağı Databaseye kaydettim")
        readme = open('README.md', 'a')
        x = str(update.message.text).replace("/kaynak", " ")
        readme.write("{}".format(update.message.from_user.first_name+" <li>" + x + "</li>"))
        readme.close()
        os.system("git add -A")
        os.system("git commit -m '" + update.message.from_user.first_name + " Link '")
        os.system("git push")
        bot.sendMessage(chat_id=update.message.chat_id, text="Url github'a eklendi.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id,text="URL HATALI")



#---------------HANDLER IS HERE--------------------

start_handler = CommandHandler('start', start)
hello_handler=CommandHandler('hello',hello)
echo_handler = MessageHandler(Filters.text, echo)
kaynak_handler=CommandHandler('kaynak',kaynak)

#--------------------------------------------------
#----------------DISPATCHER IS HERE----------------

dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(kaynak_handler)

#--------------------------------------------------

updater.start_polling()
