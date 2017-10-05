import logging

log = logging.getLogger(__name__)


def privmsg(irc, msgvars):
	log.info(msgvars["raw"])
	log.info("Dispatched PRIVMSG")
	return True

def whisper(irc, msgvars):
	log.info(msgvars["raw"])
	log.info("Dispatched WHISPER")
	return True

def usernotice(irc, msgvars):
	if msgvars["msg-id"] == "sub":
		irc.send_privmsg(
				f"NEW S U B legsHYPE Thank you @{msgvar['display-name']} for the subberino and welcome to the StrongLegsAcademy legsLOVE",
				me=True
			)

	elif msgvars["msg-id"] == "resub":
		irc.send_privmsg(
				f"REEEE S U B legsHYPE Thank you @{msgvars['display-name']} for the {msgvars['msg-param-months']} month resubscription. Thank you for the continued support! :D legsLOVE",
				me=True
			)



	log.info("Dispatched USERNOTICE")
	return True

def clearchat(irc, msgvars):
	log.info("Dispatched CLEARCHAT")
	return True

def ping(irc, msgvars):
	irc.send_raw("PONG :tmi.twitch.tv\r\n")
	log.info("Dispatched PING")
	return True
