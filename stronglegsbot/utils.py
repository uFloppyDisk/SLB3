import logging
import sys

log = logging.getLogger(__name__)


def load_config(path):
    import configparser
    import os

    cfg = configparser.ConfigParser(allow_no_value=True)

    cfg.read(path)
    cfgsections = cfg.sections()

    dictConfigValues = {}
    dictTemp = {}

    try:
        for section in cfgsections:
            options = cfg.options(section)
            if section != '':
                log.debug("reading config from section '%s'", section)
                for option in options:
                    value = cfg.get(section, option)
                    dictTemp[option] = value
                    log.debug("added variable '%s'", option)

            else:
                continue

            dictConfigValues[section] = dictTemp
            dictTemp = {}

    except Exception as err:
        log.critical("unpackconfig exception: {}", str(err))

    return dictConfigValues

def time_elapsed_ms(finish, start):
    if finish < start:
        raise ValueError

    return (finish - start) * 1000
