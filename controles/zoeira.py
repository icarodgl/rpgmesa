import random
from models import MyStick


class ZoeiraControle():
    def jogo(self):
        abobrinhas = ["RB6", "CS!", "Estudar!", "rocket league", "Lolzim"]
        return abobrinhas[random.randint(0, len(abobrinhas)-1)]

    def teco(self):
        abobrinhas = ["OLOOOOCO!", "LIXO",
                      "SEU BATATA", "Cortei o açucar", "Tóxico", ":owl: :owl: :owl: :owl: :owl: :owl:"]
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
        return allsticks[random.randint(0, len(allsticks)-1)].imagem

    def pegaStick(self, dado):
        nome = dado[1]
        thesticks = MyStick.get(MyStick.nome == nome)
        return thesticks.imagem

    def salvaStick(self, dados):
        nome = dados[1]
        imagem = dados[2]
        stick = MyStick.create(nome=nome, imagem=imagem)
        return stick.id
