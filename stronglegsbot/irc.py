import logging
import logging.handlers
import os
import socket

log = logging.getLogger(__name__)


class IRC(object):
    def __init__(self):
        self.sock = None

        self.databuffer = ""

        self.config = None
        self.conn_info = {}

        self.silent = False
        self.prefix = ""

        self.queue = None

        self.privmsg_str = "PRIVMSG {} :"

    def init(self, config):
        self.config = config

        self.conn_info = {
            "channel": self.config["settings"]["channel"],
            "username": self.config["settings"]["username"],
            "password": self.config["settings"]["password"],
            "host": self.config["settings"]["host"],
            "port": int(self.config["settings"]["port"])
        }

        self.version = self.config["debug"]["version"]

        self.silent = self.config["debug"]["silent"]
        self.prefix = self.config["debug"]["prefix"]
        self.greeting = self.config["debug"]["greeting"]
        self.privmsg_str = self.privmsg_str.format(self.conn_info["channel"])

        log.debug(f"silent set to {self.silent}")
        log.debug(f"prefix set to {self.prefix}")

    def init_connection(self, greeting=True):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(1)
            self.sock.connect((self.conn_info["host"], self.conn_info["port"]))
            self.send_raw(f'PASS {self.conn_info["password"]}\r\n')
            self.send_raw(f'NICK {self.conn_info["username"]}\r\n')
            self.send_raw(f'JOIN {self.conn_info["channel"]}\r\n')
            log.info("Joining channel '%s'", self.conn_info["channel"])

            self.send_raw('CAP REQ :twitch.tv/membership\r\n')
            self.send_raw('CAP REQ :twitch.tv/tags\r\n')
            self.send_raw('CAP REQ :twitch.tv/commands\r\n')
            self.sock.settimeout(0.01)

            if greeting and self.greeting:
                self.send_privmsg(f"VoHiYo Have no fear, StrongLegsBot (v{self.version}) is here!")

        except Exception as error:
            log.critical("irc init error:", error)

    def poll(self):
        data = ""
        temp = []
        try:
            data = self.sock.recv(1024).decode("UTF-8")
            self.databuffer = self.databuffer + data  # Appends data received to buffer
            temp = self.databuffer.rsplit('\n')  # Splits buffer into list
            self.databuffer = temp.pop()  # Grabs the last list item and assigns to buffer

        except socket.timeout:
            temp = []

        except UnicodeDecodeError as err:
            log.exception(f"{err}: {data!r}")


        return temp, data

    def reconnect(self):
        self.sock.close()
        log.warning("reconnecting socket")
        print()
        self.init_connection(False)

    def close(self):
        self.sock.close()

    def send(self, string):
        try:
            string = string.encode("UTF-8")
            bytecheck = string + b'\r\n'

            if len(bytecheck) > 2048:
                return False

            self.sock.send(string)

        except UnicodeEncodeError as UnicodeErr:
            log.error(f"socket send error: {UnicodeErr}")

    def send_raw(self, string):
        string = string.format(channel=self.conn_info["channel"])
        self.send(string)

    def send_privmsg(self, string, me=''):
        if not self.silent:
            me = ".me" if me is True else me
            string = f"{me} {self.prefix} {string}\r\n"
            self.send((self.privmsg_str + string))

        else:
            return False

    def send_whisper(self, string, to):
        if not self.silent:
            string = f".w {to} {self.prefix} {string}\r\n"
            self.send((self.privmsg_str + string))

        else:
            return False
