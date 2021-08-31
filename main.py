import logging
import sys

import telebot
import yaml

import common
import res
from img_search_google import ImageSearcher

if __name__ == '__main__':

    with open(sys.argv[1]) as yaml_file:
        cfg = yaml.safe_load(yaml_file)

    token = cfg["telegram-token"]

    telebot.logger.setLevel(logging.INFO)

    bot = telebot.TeleBot(token=token)

    searcher = ImageSearcher(cfg['google-api-key'], cfg['google-search-engine-id'])


    @bot.message_handler(commands=['img'])
    def echo_message(msg: telebot.types.Message):
        bot.send_chat_action(msg.chat.id, 'upload_photo', timeout=30)
        try:
            img = searcher.search_image(msg.text.split(sep=' ', maxsplit=1)[1])  # text goes with command itself
        except common.ImageSearchError:
            img = res.FOUND_NOTHING
        bot.send_photo(msg.chat.id, img, reply_to_message_id=msg.id)


    bot.polling()
