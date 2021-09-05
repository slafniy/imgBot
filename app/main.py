import logging
import os
import sys

import telebot

import common
import res
from img_search_google import ImageSearcher

if __name__ == '__main__':

    print(f'Env vars: {os.environ}')

    exit(0)

    telebot.logger.setLevel(logging.DEBUG)

    bot = telebot.TeleBot(token=sys.argv[1])

    searcher = ImageSearcher(sys.argv[2], sys.argv[3])


    @bot.message_handler(commands=['img'])
    def echo_message(msg: telebot.types.Message):
        bot.send_chat_action(msg.chat.id, 'upload_photo', timeout=30)
        try:
            img = searcher.search_image(msg.text.split(sep=' ', maxsplit=1)[1])  # text goes with command itself
        except common.ImageSearchError:
            img = res.FOUND_NOTHING
        bot.send_photo(msg.chat.id, img, reply_to_message_id=msg.id)


    while True:
        try:
            bot.polling(non_stop=True, timeout=60)
        except KeyboardInterrupt:
            break
        except Exception as e:
            telebot.logger.warning(f'An exception occurred: {e}\nRestarting...')
