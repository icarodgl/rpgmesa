#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
import config
from controle import Controle
from emoji import emojize
import os
import urllib.request, json
from threading import Thread
#from flask import Flask, request
#from flask_restful import Resource, Api
#from json import dumps
#app = Flask(__name__)
#api = Api(app)


# class Ligar(Resource):
#    def get(self):
#        m ={"mensagem":"estou vivo!"}
#        return m
def acorda_heroku():
    url = urllib.request.urlopen("https://rpgmesa.herokuapp.com/")
    try:
        data = json.loads(url.read().decode())
        print(data)
    except:
        print('Erro ao acordar heroku')
    
def handle(msg):
    command = emojize(msg['text'], use_aliases=True)
    acorda_heroku()
    print('Got command: %s' % command)
    controle = Controle(bot)
    #controle.comando(msg)
    worker = Thread(target=controle.comando(msg))
    worker.setDaemon(True)
    worker.start()

if __name__ == '__main__':
    bot = telepot.Bot(os.environ.get(
        'KEY_BOT', '533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8'))
    MessageLoop(bot, handle).run_as_thread()
    
    print('I am listening ...')
    while 1:
        time.sleep(10)

# lembrar que '533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8' é um codigo importante
