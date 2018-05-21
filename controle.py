#!/usr/bin/python
# -*- coding: utf-8 -*-
from controles.personagem import PersonagemControle
from controles.npc import NpcControle
from controles.ataque import ataqueControle
from controles.cenario import CenarioControle
from controles.objetos import ObjetosControle
from controles.acao import AcaoControle
from controles.drop import DropControle

class Controle(object):
    def __init__(self,bot):
        self.bot = bot
        self.chat_id = any
        self.command = any
        self.objeto = any

    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text']
        dados = self.command.split()
        comando = self.command.split()[0]
        dados =dados[1:]
        dados.insert(0,msg['from']['first_name'])
        if "/criapersonagem" in self.command:
            #/criapersonagem Nome Classe
            self.objeto = PersonagemControle()
            self.criaPersonagem(dados)
        elif "/levelup" in self.command:
            #/levelup Nome
            self.objeto = PersonagemControle()
            self.levelup(dados)
        elif "/ficha" in self.command:
            #/ficha Nome
            self.objeto = PersonagemControle()
            self.ficha(dados)
        elif comando in ["/equips","/equipamento","/eqp","/itens"]:
            #/equipamentos Nome
            self.objeto = PersonagemControle()
            self.equipamentos(dados)
        elif comando in ["/bag","/inventario","/i","/sacola","/saco"]:
            #/equipamentos Nome
            self.objeto = PersonagemControle()
            self.inventario(dados)
        elif "/crianpc" in self.command:
            #/crianpc Nome Nivel
            self.objeto = NpcControle()
            self.crianpc(dados)
        elif "/criacenario" in self.command:
            #/criacenario Nome uma descrição do mesmo
            self.objeto = CenarioControle()
            self.criacenario(dados)
        elif "/cenario" in self.command:
            #/cenario Nome
            self.objeto = CenarioControle()
            self.pegaCenario(dados)
        elif "/criaobjeto" in self.command:
            # /criaobjeto Nome Dificuldade(1 a 20) descrição
            self.objeto = ObjetosControle()
            self.criaObjeto(dados)
        elif "/ataque" in self.command:
            self.objeto = ataqueControle()
            self.ataque(dados)
        elif comando in ["/roll","/d20"]:
            #/d20 Atributo personagem
            #/roll Atributo personagem
            self.objeto = AcaoControle()
            self.d20Acao(dados)
        elif comando in ["/interage","/interagir","/cao","/ação"]:
            # 0         1           2       3
            #/interagir Personagem Objeto Ação
            self.objeto = ObjetosControle()
            self.criaAcao(dados)
        elif comando in ["/objetos","/listaobjetos","/obj"]:
            self.objeto = ObjetosControle()
            self.listaobjetos()
        elif comando in ["/limpar","/clear","/novo"]:
            self.objeto = ObjetosControle()
            self.removeobjetos()
        elif comando in ["/dropar","/criaitem","/drop"]:
            self.objeto = DropControle()
            self.criaDrop(dados)
        elif comando in ["/pega","/cat","/cata"]:
            self.objeto = DropControle()
            self.pegaDrop(dados)
        elif comando in ["/limpaDrop","/decompor"]:
            self.objeto = DropControle()
            self.limpaDrop(dados)
        elif comando in ["/ldrop","/listardrop","/drops"]:
            self.objeto = DropControle()
            self.listarDrops(dados)
    def listarDrops(self,dados):
        ret = self.objeto.listaDrop()
        self.retorna(ret)
    def limpaDrop(self,dados):
        ret = self.objeto.limpaDrop()
        self.retorna(ret)
    def pegaDrop(self,dados):
        ret = self.objeto.pegaDrop(dados)
        self.retorna(ret)
    def criaDrop(self,dados):
        ret = self.objeto.criaDrop(dados)
        self.retorna(ret)
    def removeobjetos(self):
        ret = self.objeto.limpaObjetos()
        self.retorna(ret)  
    def listaobjetos(self):
        ret = self.objeto.listaObjetos()
        self.retorna(ret)
    def levelup(self, dados):
        ret = self.objeto.levelup(dados)
        self.retorna(ret)
    def ficha(self, dados):
        ret = self.objeto.ficha(dados)
        self.retorna(ret)
    def inventario(self, dados):
        ret = self.objeto.inventario(dados)
        self.retorna(ret)
    def equipamentos (self,dados):
        ret = self.objeto.equipamentos(dados)
        self.retorna(ret)
    def d20Acao(self, dados):
        if len(dados) <= 2:
            ret = self.objeto.roll()
        else:
            if dados[1] in ["agi","agilidade"]:
                ret = self.objeto.dadoAgi(dados)
            elif dados[1] in ["dex","destreza","des"]:
                ret = self.objeto.dadoDex(dados)
            elif dados[1] in ["int","inteligencia"]:
                ret = self.objeto.dadoInt(dados)
            elif dados[1] in ["for","forca","str"]:
                ret = self.objeto.dadoFor(dados)
            elif dados[1] in ["res","resiliencia","end"]:
                ret = self.objeto.dadoRes(dados)
            else:
                ret = self.objeto.roll()
        self.retorna(ret)

    def criaObjeto(self,dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def criacenario(self,dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def pegaCenario(self,dados):
        ret = self.objeto.cenario(dados)
        self.retorna(ret)

    def crianpc(self,dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def ataque(self,dados):
        ret = self.objeto.ataque(dados)
        self.retorna(ret)

    def criaPersonagem(self,dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)
    def criaAcao(self, dados):
        ret = self.objeto.interage(dados)
        self.retorna(ret)
    def retorna(self,ret):
        self.bot.sendMessage(self.chat_id, ret)