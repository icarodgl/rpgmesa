#!/usr/bin/python3
# -*- coding: utf-8 -*-
# lembrar que '791926566:AAG8WRpd0z7JKKjhKBxTWg2QiGEcCRgy6K8' é um codigo importante
import sys
import asyncio
import telepot
from telepot.aio.loop import MessageLoop
from telepot.aio.delegate import pave_event_space, per_chat_id, create_open
from controle import Controle
from emoji import emojize
import os
from dotenv import load_dotenv
load_dotenv()

class SuperBot(telepot.aio.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(SuperBot, self).__init__(*args, **kwargs)

    async def retorna(self, ret):
        if ret is not None:
            await self.sender.sendMessage(emojize("%s" % ret, use_aliases=True))
        return

    async def retornaStick(self):
        self.sender.sendSticker( "CAADBAADpgADWSJOBYvDjrzJBxB_Ag")
        return

    async def on_chat_message(self, msg):
        controle = Controle(msg)
        await self.retorna(controle.comando())
        return


TOKEN = os.environ['BOT_KEY'] # get token from command-line


bot = telepot.aio.DelegatorBot(TOKEN, [
    pave_event_space()(
        per_chat_id(), create_open, SuperBot, timeout=10),
])

loop = asyncio.get_event_loop()
loop.create_task(MessageLoop(bot).run_forever())
print('Listening ...')

loop.run_forever()