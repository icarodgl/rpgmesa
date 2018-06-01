#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
import config
from controle import Controle
from emoji import emojize
import os 


#from flask import Flask, request
#from flask_restful import Resource, Api
#from json import dumps
#app = Flask(__name__)
#api = Api(app)


#class Ligar(Resource):
#    def get(self):
#        m ={"mensagem":"estou vivo!"}
#        return m

def handle(msg):
    command = emojize(msg['text'], use_aliases=True)
    
    print('Got command: %s' % command )
    controle = Controle(bot)
    controle.comando(msg)

if __name__ == '__main__':
    bot = telepot.Bot(os.environ.get('KEY_BOT','533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8'))
    MessageLoop(bot, handle).run_as_thread()
    print('I am listening ...')
    while 1:
        time.sleep(10)

# lembrar que '533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8' é um codigo importante