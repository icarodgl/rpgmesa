#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import telepot
from telepot.loop import MessageLoop
import config
from controle import Controle

from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps

app = Flask(__name__)
api = Api(app)


class Ligar(Resource):
    def get(self):
        m ={"mensagem":"estou vivo!"}
        return m

def handle(msg):
    command = msg['text']
    print ('Got command: %s' % command)
    controle = Controle(bot)
    controle.comando(msg)


print ('I am listening ...')
#while 1:
#    time.sleep(10)


api.add_resource(Ligar, '/')
if __name__ == '__main__':
    bot = telepot.Bot('533253560:AAHv5TaR1m3sYd4ek7jR1LSFm1ig0IeOTV8')
    MessageLoop(bot, handle).run_as_thread()
    app.run(port='5002')