#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from models import Npc, Item
class NpcControle():

    def cria(self, dados):
        classe = ""
        try:
            nome = dados[1] 
            nivel = int(dados[2])
        except:
            return "Erro, tente: /crianpc Nome Nivel"

        forca = randint(1,10)*(nivel)
        inteligencia = randint(1,10)*(nivel)
        resiliencia = randint(1,10)*(nivel)
        destreza = randint(1,10)*(nivel)
        agilidade = randint(1,10)*(nivel)
        vida=nivel*resiliencia
        try:
            npc = Npc.create(
                nome=nome,
                vida=vida,
                nivel=nivel,
                classe=classe,
                forca=forca,
                inteligencia=inteligencia,
                resiliencia=resiliencia,
                destreza=destreza,
                agilidade=agilidade
                )
        except:
            return "Erro ao criar NPC"
        return  "criado: "+str(npc.nome)+" nivel: "+str(npc.nivel)