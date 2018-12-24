import random
from models import MyStick


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

    def pegaStickAleatorio(self):
        allsticks = MyStick.select()
        return allsticks[random.randint(0, len(allsticks)-1)].id

    def pegaStick(self, dado):
        nome = dado[0]
        thesticks = MyStick.get(MyStick.nome == nome)
        return thesticks.id

    def salvaStick(self, dados):
        nome = dados[1]
        id = dados[2]
        stick = MyStick.create(nome=nome, id=id)
        return stick.id
