import os
import sys

import unittest

import constants

sys.path.append(os.path.abspath('..'))
os.chdir('..')

strings_parse = constants.strings_parse


class TestParse(unittest.TestCase):
    def test_get_identifier(self):
        from stronglegsbot.parse import get_identifier

        pos_privmsg = strings_parse["pos_privmsg"]
        pos_whisper = strings_parse["pos_whisper"]
        pos_server = strings_parse["pos_server"]

        for dict in pos_privmsg:
            self.assertEqual(get_identifier(dict["string"]), "privmsg")

        for dict in pos_whisper:
            self.assertEqual(get_identifier(dict["string"]), "whisper")

        for dict in pos_server:
            self.assertEqual(get_identifier(dict["string"]), "server")

    def test_parse_privmsg(self):
        from stronglegsbot.parse import parse_privmsg

        pos_privmsg = strings_parse["pos_privmsg"]
        check_static_msgvars = strings_parse["check_static_msgvars"]

        for dict in pos_privmsg:
            ret = parse_privmsg({}, dict["string"])

            self.assertEqual(ret["username"], check_static_msgvars["username"])
            self.assertEqual(ret["display-name"], check_static_msgvars["display-name"])
            self.assertEqual(ret["channel"], check_static_msgvars["channel"])
            self.assertEqual(ret["message"], dict["message"])

    def test_parse_whisper(self):
        from stronglegsbot.parse import parse_whisper
        
        pos_whisper = strings_parse["pos_whisper"]
        check_static_msgvars = strings_parse["check_static_msgvars"]

        for dict in pos_whisper:
            ret = parse_whisper({}, dict["string"])

            self.assertEqual(ret["username"], check_static_msgvars["username"])
            self.assertEqual(ret["display-name"], check_static_msgvars["display-name"])
            self.assertEqual(ret["message"], dict["message"])
    
    def test_parse_server(self):
        from stronglegsbot.parse import parse_server
        
        pos_server = strings_parse["pos_server"]
        check_static_msgvars = strings_parse["check_static_msgvars"]

        for dict in pos_server:
            ret = parse_server({}, dict["string"])

            if "username" in ret.keys(): self.assertEqual(ret["username"], check_static_msgvars["username"])
            if "display-name" in ret.keys(): self.assertEqual(ret["display-name"], check_static_msgvars["display-name"])
            if "message" in ret.keys(): self.assertEqual(ret["message"], dict["message"])

class TestUtils(unittest.TestCase):
    def test_time_elapsed_ms(self):
        from stronglegsbot.utils import time_elapsed_ms

        self.assertEqual(time_elapsed_ms(10, 5), 5000)
        self.assertEqual(time_elapsed_ms(5000, 1000), 4000000)
        self.assertRaises(ValueError, time_elapsed_ms, 5, 10)


if __name__ == "__main__":
    unittest.main()
