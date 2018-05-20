from random import *
from models import Npc, Item
porcentagem = .5
class NpcControle():

    def cria(self, dados):
        classe = ""
        nome = dados[2]
        nivel = dados[3]

        forca = int(randint(1,10)*(nivel*porcentagem))
        inteligencia = int(randint(1,10)*(nivel*porcentagem))
        resiliencia = int(randint(1,10)*(nivel*porcentagem)))
        destreza = int(randint(1,10)*(nivel*porcentagem))
        agilidade = int(randint(1,10)*(nivel*porcentagem))


        personagem = Npc.create(
            nome=nome,
            forca=forca,
            inteligencia=inteligencia,
            resiliencia=resiliencia,
            destreza=destreza,
            agilidade=agilidade
            )
        return personagem