from controles.personagem import PersonagemControle
from controles.npc import NpcControle
from controles.ataque import ataqueControle
from controles.cenario import CenarioControle
from controles.objetos import ObjetosControle
from controles.acao import AcaoControle

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
        dados =dados[1:]
        dados.insert(0,msg['from']['username'])

        print(self.command[0])
        if "/criapersonagem" in self.command:
            self.objeto = PersonagemControle()
            self.criaPersonagem(dados)
        elif "/crianpc" in self.command:
            self.objeto = NpcControle()
            self.crianpc(dados)
        elif "/criacenario" in self.command:
            self.objeto = CenarioControle()
            self.criacenario(dados)
        elif "/cenario" in self.command:
            self.objeto = CenarioControle()
            self.pegaCenario(dados)
        elif "/criaobjeto" in self.command:
            self.objeto = ObjetosControle()
            self.criaObjeto(dados)
        elif "/ataque" in self.command:
            self.objeto = ataqueControle()
            self.ataque(dados)
        elif self.command[0] in ["/acao","/ação"]:
            print(self.command[0])
            self.objeto = AcaoControle()
            self.acao(dados)

    def acao(self, dados):
        ret = self.objeto.interage(dados)
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

    def retorna(self,ret):
        self.bot.sendMessage(self.chat_id, ret)