#!/usr/bin/python
# -*- coding: gb2312 -*-
# https://github.com/littlecodersh/ItChat.git
# import itchat

import itchat
# from .. import itchat


@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print("print_content called ")
    print(msg['Text'])

itchat.auto_login(enableCmdQR=False)
itchat.run()

