# Parse test strings
strings_parse = {
    "check_static_msgvars": {
        "display-name": "TeSt_UseRnaMe",
        "login": "test_username",
        "username": "test_username",
        "channel": "#channel"
    },
    "pos_privmsg": [
        {
            "string":"@badges=;color=#FF0000;display-name=TeSt_UseRnaMe;emotes=;id=0cb287d7-fcdb-443c-ae5f-931e779a188f;mod=0;room-id=37402112;sent-ts=1506055573292;subscriber=0;tmi-sent-ts=1506055573051;turbo=0;user-id=123456789;user-type= :test_username!test_username@test_username.tmi.twitch.tv PRIVMSG #channel :test",
            "message": "test"
        },
        {
            "string": "@badges=;color=#FF0000;display-name=TeSt_UseRnaMe;emotes=;id=0cb287d7-fcdb-443c-ae5f-931e779a188f;mod=0;room-id=37402112;sent-ts=1506055573292;subscriber=0;tmi-sent-ts=1506055573051;turbo=0;user-id=123456789;user-type= :test_username!test_username@test_username.tmi.twitch.tv PRIVMSG #channel :test WHISPER test",
            "message": "test WHISPER test"
        },
    ],
    "pos_whisper": [
        {
            "string": "@badges=premium/1;color=#0000FF;display-name=TeSt_UseRnaMe;emotes=;message-id=1209;thread-id=37705020_118299051;turbo=1;user-id=37705020;user-type= :test_username!test_username@test_username.tmi.twitch.tv WHISPER stronglegsbot :test\r",
            "message": "test"
        },
        {
            "string": "@badges=premium/1;color=#0000FF;display-name=TeSt_UseRnaMe;emotes=;message-id=1209;thread-id=37705020_118299051;turbo=1;user-id=37705020;user-type= :test_username!test_username@test_username.tmi.twitch.tv WHISPER stronglegsbot :test PRIVMSG test\r",
            "message": "test PRIVMSG test"
        },
    ],
    "pos_server": [
        {
            "string": "@badges=subscriber/0,premium/1;color=;display-name=TeSt_UseRnaMe;emotes=;id=9a3bb8b0-4e33-45f4-9c0e-6538a4f06a97;login=test_username;mod=0;msg-id=sub;msg-param-months=1;msg-param-sub-plan-name=Channel\sSubscription\s(stronglegss);msg-param-sub-plan=Prime;room-id=95306792;subscriber=1;system-msg=TeSt_UseRnaMe\sjust\ssubscribed\swith\sTwitch\sPrime!;tmi-sent-ts=1499644008727;turbo=0;user-id=85514425;user-type= :tmi.twitch.tv USERNOTICE #channel :test WHISPER PRIVMSG test",
            "message": "test WHISPER PRIVMSG test"
        },
        {
            "string": "@badges=subscriber/0,premium/1;color=;display-name=TeSt_UseRnaMe;emotes=;id=9a3bb8b0-4e33-45f4-9c0e-6538a4f06a97;login=test_username;mod=0;msg-id=sub;msg-param-months=1;msg-param-sub-plan-name=Channel\sSubscription\s(stronglegss);msg-param-sub-plan=Prime;room-id=95306792;subscriber=1;system-msg=TeSt_UseRnaMe\sjust\ssubscribed\swith\sTwitch\sPrime!;tmi-sent-ts=1499644008727;turbo=0;user-id=85514425;user-type= :tmi.twitch.tv USERNOTICE #channel",
            "message": None
        },
    ],
}
