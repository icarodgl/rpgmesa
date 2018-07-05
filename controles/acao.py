#!/usr/bin/python3
# -*- coding: utf-8 -*-
from models import Personagem
import random
class AcaoControle():
    def roll(self):
        return "D20: "+str(random.randint(1,20))
    def dadoAgi(self, dados):
        personagem = self.getPersonagem(dados[0])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.agilidade)
        return "%s Tirou: %d em agilidade"%(personagem.nome,d20)

    def dadoDex(self, dados):

        personagem = self.getPersonagem(dados[0])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.destreza)
        return "%s Tirou: %d em destreza"%(personagem.nome,d20)

    def dadoInt(self, dados):

        personagem = self.getPersonagem(dados[0])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.inteligencia)
        return "%s Tirou: %d em inteligencia"%(personagem.nome,d20)

    def dadoFor(self, dados):
        personagem = self.getPersonagem(dados[0])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.forca)
        return "%s Tirou: %d em força"%(personagem.nome,d20)

    def dadoRes(self, dados):

        personagem = self.getPersonagem(dados[0])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.resiliencia)
        return "%s Tirou: %d em resiliencia"%(personagem.nome,d20)

    def getPersonagem(self, nome):
        try:
            return Personagem.get(Personagem.usuario == nome)
        except :
            return None
    def jogaD20(self,quantidade):
        return quantidade + random.randint(1, 20)
        
        