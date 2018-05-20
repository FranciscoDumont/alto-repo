#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from random import randint

from xd.message_filter import *
from xd.emojiador import Emojiador
from xd.mensaje_random import *

from random import randint

from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

update_id = None


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

emojiador = Emojiador()
mensaje_random = MensajeRandom()
happy_filter = HappyFilter()
todo_filter = TodoFilter()


def main():

    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("606589324:AAFynsBS23okwvi6vN8CBtGDOmYd_kZ2wFo")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_handler(MessageHandler(happy_filter, compro))

    """Este filter siempre tiene que estar ultimo"""
    dp.add_handler(MessageHandler(todo_filter, random))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

def echo(bot,update):
    """Echo the user message."""
    update.message.reply_text(emojize(emojiador.textToEmoji(update.message.text),use_aliases=True ))


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def start(bot, update):
    update.message.reply_text('que onda bro? estoy re en pedo ya')

def compro(bot,update):
    chat_id = update.message.chat.id
    user_id = update.message.from_user.id
    bot.send_message(chat_id=update.message.chat.id, text="COMPRO!!",reply_to_message_id=update.message.message_id)

def random(bot,update):
    """Hay un 1/20 de probabilidad que responda alguna frase random"""
    if randint(0,20)==1:
        update.message.reply_text(mensaje_random.fraseRandom() )



if __name__ == '__main__':
    main()
