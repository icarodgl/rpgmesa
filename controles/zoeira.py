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
    
    def hara(self):
        abobrinhas = ["Iraque!",
                      "Tá careca de saber",
                      "Aranha arranha a rã"
                     ]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def tadeu(self):
        abobrinhas = ["Kolkamente!",
                      "KOOOOOOLKE!"
                     ]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def carlos(self):
        abobrinhas = ["Só Carlitada!",
                      "Trollitos!!"
                     ]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def yan(self):
        abobrinhas = ["Abandonou o curso?","Foi pra Russia?"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def marcos(self):
        abobrinhas = ["Marcuxo!", 
                      "Barry Allen", 
                      "The fastest man alive!"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def douglas(self):
        abobrinhas = [":owl:",
                      "Corujão",
                      ":bike:"
                     ]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def teco(self):
        abobrinhas = ["OLOOOOCO!",
                      "LIXO",
                      "SEU BATATA",
                      "Tóxico",
                      ":owl: :owl: :owl: :owl: :owl: :owl:",
                      "Carlitada no Calhau"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def rage(self):
        abobrinhas = ["LIXO",
                      "tá na Disney",
                      "Troll",
                      "SEU BATATA",
                      "Tóxico",
                      "Minecraft do carai"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
    def feliz(self):
        abobrinhas = ["OLOOOOCO!",
                      "Corujão do esporte :owl:",
                      ":owl: :owl: :owl: :owl: :owl: :owl:",
                      "Do latim strategy"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
