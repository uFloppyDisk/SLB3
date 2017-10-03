import logging

log = logging.getLogger(__name__)


def privmsg(msgvars):
	log.info(msgvars["raw"])
	log.info("Dispatched PRIVMSG")
	return True

def whisper(msgvars):
	log.info(msgvars["raw"])
	log.info("Dispatched WHISPER")
	return True

def usernotice(msgvars):
	log.info("Dispatched USERNOTICE")
	return True

def clearchat(msgvars):
	log.info("Dispatched CLEARCHAT")
	return True

def ping(msgvars):
    log.info("Dispatched PING")
    return True
