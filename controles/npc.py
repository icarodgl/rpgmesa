#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from models import Npc, Item
from controles.mestre import MestreControle


class NpcControle():

    def cria(self, dados):
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre"

        classe = ""
        try:
            nome = dados[1]
            nivel = int(dados[2])
        except:
            return "Erro, tente: /crianpc Nome Nivel"

        forca = randint(1, 20) + (nivel)
        inteligencia = randint(1, 20) + (nivel)
        resiliencia = randint(1, 20) + (nivel)
        destreza = randint(1, 20) + (nivel)
        agilidade = randint(1, 20) + (nivel)
        vida = nivel * resiliencia
        try:
            npc = Npc.create(
                nome=nome,
                vida=vida,
                vidamax=vida,
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
        return "criado: " + str(npc.nome) + " nivel: " + str(npc.nivel)

    def listaNpc(self, dados):
        try:
           npcs = Npc.select()
        except:
            return "Não existe npc no jogo."
        res = "NPCs: \n"
        res = "> Nome: nivel, vida, for, agi, dex, int, res"
        for npc in npcs:
            res+= "> %s: %d, [%d/%d], %d, %d, %d, %d, %d" % (npc.nome , npc.nivel, npc.vida,npc.vidamax, npc.forca,npc.agilidade,npc.destreza,npc.inteligencia,npc.resiliencia)
        return res