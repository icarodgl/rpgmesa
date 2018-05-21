#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
import config
from controle import Controle

def handle(msg):
    command = msg['text']
    print ('Got command: %s' % command)
    controle = Controle(bot)
    controle.comando(msg)

bot = telepot.Bot('533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8')
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')
while 1:
    time.sleep(10)