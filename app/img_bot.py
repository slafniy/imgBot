import argparse
import logging
import pathlib
import time

import telebot
import yaml

import common
import res
from img_search_google import ImageSearcher


RETRIES_NUMBER = 5
RETRIES_TIMEOUT = 5

logger = common.Logger('MainLogger', logging.INFO)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()

    argument_parser.add_argument('-c', '--config', type=str, dest='configuration',
                                 help='Configuration file path',
                                 default=str(pathlib.Path(__file__).parent / 'cfg.yaml'))
    argument_parser.add_argument('--telegram-token', dest='telegram_token',
                                 help='Override telegram_token from configuration')
    argument_parser.add_argument('--google-api-key', dest='google_api_key',
                                 help='Override google_api_key from configuration')
    argument_parser.add_argument('--google-search-id', dest='google_search_id',
                                 help='Override google_search_id from configuration')
    args = argument_parser.parse_args()

    with open(args.configuration) as yaml_file:
        cfg = yaml.safe_load(yaml_file)

    token = cfg["telegram_token"]

    telebot.logger.setLevel(logging.INFO)

    bot = telebot.TeleBot(token=token)

    searcher = ImageSearcher(cfg['google_api_key'], cfg['google_search_id'])


    @bot.message_handler(commands=['img'])
    def echo_message(msg: telebot.types.Message):
        q = msg.text.split(sep=' ', maxsplit=1)[1]
        try:
            img = searcher.search_image(q)  # text goes with command itself
        except common.ImageSearchError:
            img = res.FOUND_NOTHING

        for i in range(1, RETRIES_NUMBER):
            try:
                with logger.measure_time(f'Sending image for {q}, try #{i}'):
                    bot.send_chat_action(msg.chat.id, 'upload_photo', timeout=30)
                    bot.send_photo(msg.chat.id, img, reply_to_message_id=msg.id)
            except Exception as e:
                logger.error(f'Image sending error ({q}): {e}')
                time.sleep(RETRIES_TIMEOUT)
            else:
                break


    while True:
        try:
            bot.polling(non_stop=True)
        except Exception as e:
            telebot.logger.warning(f'An exception occurred: {e}\nRestarting...')
        else:
            break  # polling() handles KeyboardInterrupt inside
