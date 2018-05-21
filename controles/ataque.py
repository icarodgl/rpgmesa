#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import *
from models import Npc, Item, Personagem
from peewee import *

class ataqueControle():
    def ataque(self,dados):
        try:
            atacante = dados[1]
            atacado = dados[2]
        except:
            return "Erro tente: /ataque atacante atacado"
        try:
            atacante = Personagem.get(Personagem.nome == atacante)
        except:
            try:
                atacante = Npc.get(Npc.nome == atacante)
            except:    
                return "Erro: "+atacante+"=> inexistente"
        try:
            atacado = Npc.get(Npc.nome == atacado)
        except:
            try:
                atacado = Personagem.get(Personagem.nome == atacado)
            except:
                return "Erro: =>"+atacado+" inexistente"

        dano = atacante.forca
        #dano+= atacante.bra_dir.ataque
        #dano+= atacante.bra_esq.ataque
        atacado.vida = atacado.vida - dano
        if atacado.save() :
            resultado = str(atacado.nome)+" recebeu "+str(dano)+" e ficou com: "+str(atacado.vida)+" de vida"
            return resultado
        else:
            return "ataque falhou 2"
        