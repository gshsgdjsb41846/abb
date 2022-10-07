from telegram.ext import *

def stm(u,c):
    u.message.reply_text("Bruhh")

def stt(u,c):
    u.message.reply_text("Choltase bhy bot")


upt = Updater("5666523095:AAFnqmsrwqosN0m-WRRDbEdHMZg6q2a39to", use_context=True)

upt.dispatcher.add_handler(CommandHandler("start",stm))
upt.dispatcher.add_handler(CommandHandler("status",stt))

upt.start_polling()
upt.idle()
