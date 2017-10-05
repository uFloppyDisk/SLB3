import logging
import socket
import time
import os

import stronglegsbot.dispatch
import stronglegsbot.irc
import stronglegsbot.parse
from stronglegsbot.utils import load_config
from stronglegsbot.utils import time_elapsed_ms

log = logging.getLogger(__name__)


class BOT(object):
    def __init__(self):
        self.exit = False

        self.config = {}

    def __repr__(self):
        channel = self.config["settings"]["channel"]
        prefix = self.config["debug"]["prefix"]
        silent = self.config["debug"]["silent"]
        greeting = self.config["debug"]["greeting"]
        return(f"class BOT(channel={channel},prefix={prefix},silent={silent},greeting={greeting})")

    def init(self, channel="", prefix="", silent="", greeting=""):
        self.config = load_config(".\cfg\config.ini")

        # Check to see if args were declared, if not default to config values
        self.config["settings"]["channel"] = channel if channel != "" else self.config["settings"]["channel"]
        self.config["debug"]["prefix"] = prefix if prefix != "" else self.config["debug"]["prefix"]
        self.config["debug"]["silent"] = silent if silent != "" else self.config["debug"]["silent"]
        self.config["debug"]["greeting"] = greeting if greeting != "" else self.config["debug"]["greeting"]

        self.irc = stronglegsbot.irc.IRC()
        self.irc.init(self.config)
        self.irc.init_connection()

    def conn_close(self):
        self.irc.close()

    def conn_reconnect(self):
        self.irc.reconnect()

    def dispatch(self, msgvars):
        try:
            dispatch_func = getattr(stronglegsbot.dispatch, msgvars["msgtype"])
        except AttributeError:
            log.warning("Dispatch not found for %s", msgvars["msgtype"].upper())
            return

        log.debug("Dispatching...")
        feedback = dispatch_func(self.irc, msgvars)
        return feedback

    def main(self):
        while not self.exit:
            temp, data = self.irc.poll()

            for line in temp:
                if len(data) == 0:
                    self.conn_reconnect()
                    break

                start_tick = time.time()

                msgtype = stronglegsbot.parse.get_identifier(line)
                msgvars = stronglegsbot.parse.parse(msgtype, line)
                # parse = getattr(stronglegsbot.parse, f"parse_{msgtype}")
                # msgvars = parse(line)

                if msgvars["msgtype"]:
                    feedback = self.dispatch(msgvars)
                else:
                    log.warning(f"no dispatch for: {line}")

                finish_tick = time.time()
                elapsed_ms = time_elapsed_ms(start=start_tick, finish=finish_tick)

                if elapsed_ms >= 5:
                    log.warning(f"Message took {elapsed_ms:1.5}ms to finish: {line}")

                else:
                    log.info(f"Finished in {elapsed_ms:1.3} ms")
