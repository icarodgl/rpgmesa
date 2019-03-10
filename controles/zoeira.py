import random
from models import MyStick


class ZoeiraControle():
    def jogo(self):
        abobrinhas = ["Tem :owl: lá tambem?",
                      "Aquele famoso: Hj nem da pra mim",
                      "Estudar!",
                      "10 min",
                      "23h30 +10min"
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