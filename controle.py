#!/usr/bin/python3
# -*- coding: utf-8 -*-
from controles.personagem import PersonagemControle
from controles.npc import NpcControle
from controles.ataque import ataqueControle
from controles.cenario import CenarioControle
from controles.objetos import ObjetosControle
from controles.acao import AcaoControle
from controles.drop import DropControle
from controles.mestre import MestreControle
from emoji import emojize
from controles.help import AjudaControle
import telegram

 
class Controle(object):
    def __init__(self, bot):
        self.bot = bot
        self.chat_id = any
        self.command = any
        self.objeto = any

    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text']
        dados = self.command.split()
        comando = self.command.split()[0]
        dados = dados[1:]
        dados.insert(0, msg['from']['first_name'] + " " + msg['from']["last_name"])
        for d in range(len(dados)):
            dados[d] = dados[d].lower()
        if "/criapersonagem" in self.command:
            self.objeto = PersonagemControle()
            self.criaPersonagem(dados)
        elif "/levelup" in self.command:
            self.objeto = PersonagemControle()
            self.levelup(dados)
        elif "/ficha" in self.command:
            self.objeto = PersonagemControle()
            self.ficha(dados)
        elif comando in ["/equipar", "/equipa"]:
            self.objeto = PersonagemControle()
            self.equipar(dados)
        elif comando in ["/equips", "/equipamentos", "/equipamento", "/e"]:
            self.objeto = PersonagemControle()
            self.equipamentos(dados)
        elif comando in ["/bag", "/inventario", "/i", "/sacola", "/saco"]:
            self.objeto = PersonagemControle()
            self.inventario(dados)
        elif comando in ["/ncria", "/crianpc","/npc"]:
            self.objeto = NpcControle()
            self.crianpc(dados)
        elif "/criacenario" in self.command:
            self.objeto = CenarioControle()
            self.criacenario(dados)
        elif "/cenario" in self.command:
            self.objeto = CenarioControle()
            self.pegaCenario(dados)
        elif comando in ["/criao", "/criaobjeto","/criaobjetos"] :
            self.objeto = ObjetosControle()
            self.criaObjeto(dados)
        elif comando in ["/npcatacar", "/npcataque", "/nataque","/na"]:
            self.objeto = ataqueControle()
            self.ataquenpc(dados)
        elif comando in ["/atacar", "/ataque", "/atk"]:
            self.objeto = ataqueControle()
            self.ataque(dados)
        elif comando in ["/roll", "/d20"]:
            self.objeto = AcaoControle()
            self.d20Acao(dados)
        elif comando in ["/interage", "/interagir", "/ação"]:
            self.objeto = ObjetosControle()
            self.criaAcao(dados)
        elif comando in ["/objetos", "/lobjetos", "/lo"]:
            self.objeto = ObjetosControle()
            self.listaobjetos()
        elif comando in ["/limpar", "/clear", "/novo"]:
            self.objeto = ObjetosControle()
            self.removeobjetos()
        elif comando in ["/dropar", "/criaitem", "/drop"]:
            self.objeto = DropControle()
            self.criaDrop(dados)
        elif comando in ["/pega", "/cat", "/pegar"]:
            self.objeto = DropControle()
            self.pegaDrop(dados)
        elif comando in ["/limpaDrop", "/decompor"]:
            self.objeto = DropControle()
            self.limpaDrop(dados)
        elif comando in ["/ldrop", "/listardrop", "/drops"]:
            self.objeto = DropControle()
            self.listarDrops(dados)
        elif comando in ["/doar"]:
            self.objeto = PersonagemControle()
            self.doar(dados)
        elif comando in ["/sleep", "/dormir", "/soneca", "/descansar"]:
            self.objeto = PersonagemControle()
            self.dormir(dados)
        elif comando in ["/add","/atributos","/+"]:
            self.objeto = PersonagemControle()
            self.add(dados)
        elif comando in ["/querosermestre"]:
            self.objeto = MestreControle()
            self.addmestre(dados)
        elif comando in ["/deletarpersonagem"]:
            self.objeto = PersonagemControle()
            self.deletarpersonagem(dados)
        elif comando in ["/killall", "/matartodos","/matatudo"]:
            self.objeto = MestreControle()
            self.killall(dados)
        elif comando in ["/killnpc", "/matanpc","/matar"]:
            self.objeto = MestreControle()
            self.killnpc(dados)
        elif comando in ["/deixarmestre"]:
            self.objeto = MestreControle()
            self.addmestre(dados)
        elif comando in ["/listanpc","/lnpc"]:
            self.objeto = NpcControle()
            self.listanpc(dados)
        elif comando in ["/help","/h","/ajuda"]:
            self.objeto = AjudaControle()
            self.ajuda(dados)
        elif comando in ["/helpm","/hm","/ajudam"]:
            self.objeto = AjudaControle()
            self.ajudam(dados)
        else:
            ret = "comando '%s' não existe use /help :scream:" % comando
            self.teclado(ret)

    def ajuda(self, dados):
        ret = self.objeto.ajuda(dados)
        self.retorna(ret)
    def ajudam(self, dados):
        ret = self.objeto.ajudaM(dados)
        self.retorna(ret)
    def listanpc(self, dados):
        ret = self.objeto.listaNpc(dados)
        self.retorna(ret)
    def deletarpersonagem(self,dados):
        ret = self.objeto.deletarPersonagem(dados)
        self.retorna(ret)
    def addmestre(self, dados):
        ret = self.objeto.addMestre(dados)
        self.retorna(ret)
    def killall(self, dados):
        ret = self.objeto.killall(dados)
        self.retorna(ret)
    def killnpc(self, dados):
        ret = self.objeto.killNpc(dados)
        self.retorna(ret)
    def killmestre(self, dados):
        ret = self.objeto.killMestre(dados)
        self.retorna(ret)

    def add(self, dados):
        ret = self.objeto.addatributo(dados)
        self.retorna(ret)

    def doar(self, dados):
        ret = self.objeto.darPontos(dados)
        self.retorna(ret)

    def dormir(self, dados):
        ret = self.objeto.dormir(dados)
        self.retorna(ret)

    def equipar(self, dados):
        ret = self.objeto.equipar(dados)
        self.retorna(ret)

    def listarDrops(self, dados):
        ret = self.objeto.listaDrop()
        self.retorna(ret)

    def limpaDrop(self, dados):
        ret = self.objeto.limpaDrop()
        self.retorna(ret)

    def pegaDrop(self, dados):
        ret = self.objeto.pegaDrop(dados)
        self.retorna(ret)

    def criaDrop(self, dados):
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

    def equipamentos(self, dados):
        ret = self.objeto.equipamentos(dados)
        self.retorna(ret)

    def d20Acao(self, dados):
        if len(dados) <= 2:
            ret = self.objeto.roll()
        else:
            if dados[1] in ["agi", "agilidade"]:
                ret = self.objeto.dadoAgi(dados)
            elif dados[1] in ["dex", "destreza", "des"]:
                ret = self.objeto.dadoDex(dados)
            elif dados[1] in ["int", "inteligencia"]:
                ret = self.objeto.dadoInt(dados)
            elif dados[1] in ["for", "forca", "str"]:
                ret = self.objeto.dadoFor(dados)
            elif dados[1] in ["res", "resiliencia", "end"]:
                ret = self.objeto.dadoRes(dados)
            else:
                ret = self.objeto.roll()
        self.retorna(ret)

    def criaObjeto(self, dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def criacenario(self, dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def pegaCenario(self, dados):
        ret = self.objeto.cenario(dados)
        self.retorna(ret)

    def crianpc(self, dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def ataque(self, dados):
        ret = self.objeto.ataque(dados)
        self.retorna(ret)
    def ataquenpc(self, dados):
        ret = self.objeto.ataquenpc(dados)
        self.retorna(ret)
    def criaPersonagem(self, dados):
        ret = self.objeto.cria(dados)
        self.retorna(ret)

    def criaAcao(self, dados):
        ret = self.objeto.interage(dados)
        self.retorna(ret)

    def retorna(self, ret):
        self.bot.sendMessage(self.chat_id, emojize("` %s `" %ret, use_aliases=True))
    def teclado(self,ret):
        custom_keyboard = [['top-left', 'top-right'],['bottom-left', 'bottom-right']]
        reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
        bot.send_message(chat_id=chat_id, 
                        text="Custom Keyboard Test", 
                        reply_markup=reply_markup)