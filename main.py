import sys

import telebot


if __name__ == '__main__':
    token = sys.argv[1]
    print(f'Connecting with token {token}')
    bot = telebot.TeleBot(token=token)

    @bot.message_handler()
    def echo_message(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, f'You said {msg.text}')


    bot.polling()
