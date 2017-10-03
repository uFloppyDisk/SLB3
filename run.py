import argparse
import logging
import os
import time
import socket
import sys

import stronglegsbot.bot as stronglegsbot

try:
    basestring
except NameError:
    basestring = str


def init_bot():
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-c", "--channel", default="", type=str, required=False, help="IRC channel to join")
    arg_parser.add_argument("-p", "--prefix", default="", type=str, required=False, help="String to go before every chat message or whisper")
    arg_parser.add_argument("-l", "--log", choices=['debug', 'info', 'warning', 'error', 'critical'], default="info", type=str, required=False, help="Set minimum logging level for messages to be logged to console")
    arg_parser.add_argument("-s", "--silent", action='store_true', help="Disable chat messages")
    arg_parser.add_argument("-g", "--nogreeting", action='store_false', help="Don't send greeting to chat upon join")

    args = arg_parser.parse_args()

    logging_levels = {
        "debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING,
        "error": logging.ERROR, "critical": logging.CRITICAL
    }

    logging.basicConfig(format='<%(asctime)s> :%(name)s:%(lineno)s: [%(levelname)s] %(message)s', level=logging_levels[args.log])
    log = logging.getLogger(__name__)

    file_log = logging.FileHandler("logs/temp/errors.log")
    file_log.setLevel(logging.WARNING)

    log.addHandler(file_log)

    bot = stronglegsbot.BOT()
    bot.init(channel=args.channel, prefix=args.prefix, silent=args.silent, greeting=args.nogreeting)

    log.debug(repr(bot))

    try:
        bot.main()

    except KeyboardInterrupt:
        bot.conn_close()
        log.info("Program terminated (KeyboardInterrupt)")
        sys.exit()

    except Exception as exc:
        log.exception(f"Unhandled exception: {exc}")


if __name__ == "__main__":
    init_bot()
