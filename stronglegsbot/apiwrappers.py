import json
import logging
import urllib.requests

import requests

log = logging.getLogger(__name__)

class APIBase:
    def __init__(self, strict=False):
        self.strict = strict

    def _get(self, url, headers={}):
        try:
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req, timeout=30)

        except urllib.error.HTTPError as error:
            if self.strict:
                raise error
            else:
                return None

        except:
            log.exception("Unhandled exception in APIBase._get")

        try:
            return response.read().decode("utf-8")
        except:
            log.exception("Unhandled exception in APIBase._get while reading response")
            return None

        return None
