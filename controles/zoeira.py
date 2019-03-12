import random
import datetime
from models import MyStick
import pytz


class ZoeiraControle():
    def jogo(self):
        date =  datetime.datetime.now(pytz.timezone('America/Sao_Paulo'))
        abobrinhas = ["Tem :owl: lá tambem?",
                      "Hj nem da pra mim",
                      "10 min",
                      "%s +10min" %(date.strftime("%H:%M"))
                      ]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def teco(self):
        abobrinhas = ["OLOOOOCO!",
                      "LIXO",
                      "SEU BATATA",
                      "Tóxico",
                      ":owl: :owl: :owl: :owl: :owl: :owl:"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def rage(self):
        abobrinhas = ["LIXO",
                      "tá na Disney",
                      "Troll",
                      "SEU BATATA",
                      "Tóxico"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def feliz(self):
        abobrinhas = ["OLOOOOCO!",
                      "Corujão do esporte :owl:",
                      ":owl: :owl: :owl: :owl: :owl: :owl:"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
