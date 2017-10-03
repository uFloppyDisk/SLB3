import time
import logging
import sys

thismodule = sys.modules[__name__]

log = logging.getLogger(__name__)

def get_identifier(string):
    if " PRIVMSG " in string and " PRIVMSG " in string.split(" :", 2)[1]:
        return "privmsg"

    elif " WHISPER " in string and " WHISPER " in string.split(" :", 2)[1]:
        return "whisper"

    else:
        return "server"


def parse(identifer, string):
    msgvars = {}
    msgvars["raw"] = string
    parse_method = getattr(thismodule, f"parse_{identifer}")
    msgvars = parse_method(msgvars, string)

    return msgvars

def parse_tags(msgvars, string):
    string_split = string.strip('@').split(" :", 1)

    tags = string_split[0].split(';')

    for tag in tags:
        tag_split = tag.split('=')
        msgvars[tag_split[0]] = tag_split[1]

    return msgvars, string_split

def parse_privmsg(msgvars, string):
    try:
        msgvars, string_split = parse_tags(msgvars, string)

        tmi, info = string_split[1].split(" PRIVMSG ")
        info = info.split(" :")
        msgvars["username"] = tmi.split('!')[0]
        msgvars["channel"] = info[0]
        msgvars["message"] = info[1].strip('\r')
        msgvars["msgtype"] = "privmsg"
        msgvars["shortmsgtype"] = "priv"

        return msgvars

    except Exception as error:
        log.exception("parse privmsg exception:", error)

def parse_whisper(msgvars, string):
    try:
        msgvars, string_split = parse_tags(msgvars, string)

        tmi, info = string_split[1].split(" WHISPER ")
        info = info.split(" :")
        msgvars["username"] = tmi.split('!')[0]
        msgvars["message"] = info[1].strip('\r')
        msgvars["msgtype"] = "whisper"
        msgvars["shortmsgtype"] = "whis"

        return msgvars

    except Exception as error:
        log.exception("parse whisper exception:", error)

def parse_server(msgvars, string):
    if string.startswith('@'):
        msgvars, string_split = parse_tags(msgvars, string)

    if " USERNOTICE " in string and " USERNOTICE " in string.split(" :", 2)[1]:
        tmi, info = string_split[1].split(" USERNOTICE ")
        info = info.split(" :")
        msgvars["channel"] = info[0]
        msgvars["message"] = info[1].strip('\r') if len(info) > 1 else None
        msgvars["msgtype"] = "usernotice"
        msgvars["shortmsgtype"] = "usnt"

        return msgvars

    elif "PING" in string:
        msgvars["msgtype"] = msgvars["shortmsgtype"] = "ping"
        return msgvars

    elif "CLEARCHAT" in string:
        msgvars["msgtype"] = "clearchat"
        msgvars["shortmsgtype"] = "clch"
        return msgvars

    elif "GLOBALUSERSTATE" in string:
        msgvars["msgtype"] = "globaluserstate"
        msgvars["shortmsgtype"] = "glus"
        return msgvars

    elif "HOSTTARGET" in string:
        msgvars["msgtype"] = "hosttarget"
        msgvars["shortmsgtype"] = "host"
        return msgvars

    elif "JOIN" in string:
        msgvars["msgtype"] = msgvars["shortmsgtype"] = "join"
        return msgvars

    elif "MODE" in string:
        msgvars["msgtype"] = msgvars["shortmsgtype"] = "mode"
        return msgvars

    elif "NOTICE" in string:
        msgvars["msgtype"] = "notice"
        msgvars["shortmsgtype"] = "note"
        return msgvars

    elif "PART" in string:
        msgvars["msgtype"] = msgvars["shortmsgtype"] = "part"
        return msgvars

    elif "RECONNECT" in string:
        msgvars["msgtype"] = "reconnect"
        msgvars["shortmsgtype"] = "recn"
        return msgvars

    elif "ROOMSTATE" in string:
        msgvars["msgtype"] = "roomstate"
        msgvars["shortmsgtype"] = "rmst"
        return msgvars

    elif "USERSTATE" in string:
        msgvars["msgtype"] = "userstate"
        msgvars["shortmsgtype"] = "urst"
        return msgvars

    else:
        if "msgtype" not in msgvars.keys():
            msgvars["msgtype"] = False
            msgvars["shortmsgtype"] = "unid"

    return msgvars
