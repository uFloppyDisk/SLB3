import configparser
import logging
import os

log = logging.getLogger(__name__)
# module_log.setLevel(logging.DEBUG)

cfg = configparser.ConfigParser(allow_no_value=True)


class ConfigUnpacker:
    def __init__(self):
        self.dictConfigValues = {}

    def unpackcfg(self):
        cfg.read("..\cfg\config.ini")
        cfgsections = cfg.sections()
        try:
            for section in cfgsections:
                options = cfg.options(section)
                if section != '':
                    log.debug("reading config from section '%s'", section)
                    for option in options:
                        value = cfg.get(section, option)
                        self.dictConfigValues['%s_%s' % (section, option)] = value
                        log.debug("added variable '%s'", option)

        except Exception as err:
            log.critical("unpackconfig exception:", err)

        return self.dictConfigValues


if __name__ == "__main__":
    pass
