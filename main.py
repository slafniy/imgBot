import time
import sys

import telebot

from img_search_selenium import ImageSearcher

if __name__ == '__main__':
    token = sys.argv[1]
    print(f'Connecting with token {token}')
    bot = telebot.TeleBot(token=token)

    searcher = ImageSearcher()


    @bot.message_handler(commands=['img'])
    def echo_message(msg: telebot.types.Message):
        end = time.time() + 10
        while time.time() < end:
            try:
                bot.send_photo(msg.chat.id, searcher.search_image(msg.text), reply_to_message_id=msg.id)
                break
            except Exception as e:
                bot.send_message(msg.chat.id, f'Shit happened: {e}', reply_to_message_id=msg.id)
    bot.polling()
