import random


class ZoeiraControle():
    def teco(self):
        abobrinhas = ["OLOOOOCO!", "LIXO",
                      "SEU BATATA", "Cortei o açucar", "Tóxico"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def doug(self):
        abobrinhas = ["CS!", "PARTIU LOLZIM", "tá tudo aqui ó  :wink::point_left:",
                      "Mano téco é muito sem noção", "Tóxico"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def hara(self):
        abobrinhas = ["paçoca", "coé", "hã", "coé", "Tóxico"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]
