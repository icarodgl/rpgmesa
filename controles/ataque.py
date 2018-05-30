#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import randint
from models import Npc, Item, Personagem
from controles.mestre import MestreControle
from peewee import *

class ataqueControle():
    
    def dano (self):
        dmg = 0
        try:
            dmg += Item.get_by_id(self.atacante.bra_dir).ataque
            dmg += Item.get_by_id(self.atacante.bra_esq).ataque
            dmg += Item.get_by_id(self.atacante.cabeca).ataque
            dmg += Item.get_by_id(self.atacante.peito).ataque
            dmg += Item.get_by_id(self.atacante.perna).ataque
            dmg += Item.get_by_id(self.atacante.sapato).ataque
            
        except IntegrityError :
            pass
        dmg = randint(self.atacante.forca, self.atacante.forca + dmg) 
        return dmg
    def defesa (self):
        defesa = 0
        try:
            defesa += Item.get_by_id(self.atacado.bra_dir).defesa
            defesa += Item.get_by_id(self.atacado.bra_esq).defesa
            defesa += Item.get_by_id(self.atacado.cabeca).defesa
            defesa += Item.get_by_id(self.atacado.peito).defesa
            defesa += Item.get_by_id(self.atacado.perna).defesa
            defesa += Item.get_by_id(self.atacado.sapato).defesa
            
        except IntegrityError:
            pass
        defesa = randint(self.atacado.resiliencia, self.atacado.resiliencia + defesa)
        return defesa
    def ataque(self,dados):
        defesa = 0
        dano = 0
        npc = False
        try:
            usuario = dados[0]
            atacado = dados[1]
        except:
            return "Erro tente: /ataque Inimigo"
        try:
            self.atacante =  Personagem.get(Personagem.usuario == usuario)
        except IntegrityError:
            return "ERRO, "+usuario+" não possui personagem"
        try:
            self.atacado = Npc.get(Npc.nome == atacado)
            defesa = self.atacado.resiliencia
            npc = True
        except :
            try:
                self.atacado = Personagem.get(Personagem.nome == atacado)
                try:
                    defesa = self.defesa()
                except IntegrityError:
                    pass
            except:
                return "Erro: "+atacado+" inexistente"
        dex = self.atacado.destreza + randint(1,20)
        agi = self.atacante.agilidade + randint(1,20)
        if (agi > dex):
            return "%s Esquivou de %s  \n[dex/agi]\n(%d/%d)" %(self.atacado.nome,self.atacante.nome,dex,agi)

        try:
            dano = self.dano()
        except IntegrityError:
            pass
        dmg =(dano - defesa)
        if dmg > 0:
            self.atacado.vida = self.atacado.vida - dmg
            if self.atacado.save() :
                resultado = str(self.atacado.nome)+" recebeu "+str(dmg)+" e ficou com: "+str(self.atacado.vida)+" de vida :collision:"
                if self.atacado.vida <= 0:
                    resultado += "\n %s morreu." % self.atacado.nome
                    if npc:
                        self.atacado.delete_instance()
                return resultado
        else:
            return "%s não deu %d de dano para atingir %s que defendeu %d"%(self.atacante.nome,dano,self.atacado.nome, defesa)

    def ataquenpc(self, dados):
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre"

        defesa = 0
        dano = 0
        npc = False
        try:
            npc = dados[1]
            atacado = dados[2]
        except:
            return "Erro tente: /npcataque npc personagem"
        try:
            self.atacante = Npc.get(Npc.nome == npc)
        except IntegrityError:
            return "ERRO, " + npc + " não é um npc"
        try:
            self.atacado = Npc.get(Npc.nome == atacado)
            defesa = self.atacado.resiliencia
            npc = True
        except:
            try:
                self.atacado = Personagem.get(Personagem.nome == atacado)
                try:
                    defesa = self.defesa()
                except :
                    return "Erro na defesa"
            except :
                return "Erro: " + atacado + " inexistente"
        dex = self.atacado.destreza + randint(1, 20)
        agi = self.atacante.agilidade + randint(1, 20)
        if (agi > dex):
            return "%s Esquivou de %s  \n[dex/agi]\n(%d/%d)" % (self.atacado.nome, self.atacante.nome, dex, agi)
        dano = (self.atacante.forca + randint(1, self.atacante.nivel))
        dmg = (dano - defesa)
        if dmg > 0:
            self.atacado.vida = self.atacado.vida - dmg
            if self.atacado.save():
                resultado = str(self.atacado.nome) + " recebeu " + str(dmg) + " e ficou com: " + str(
                    self.atacado.vida) + " de vida"
                if self.atacado.vida <= 0:
                    resultado += "\n %s morreu." % self.atacado.nome
                    if npc:
                        self.atacado.delete_instance()
                return resultado
        else:
            return "%s não teve dano suficiente para atingir %s [atk/def](%d/%d)" % (
            self.atacante.nome, self.atacado.nome, dano, defesa)
