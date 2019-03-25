#!/usr/bin/python3
# -*- coding: utf-8 -*-
from typing import Any

from controles.dados import DadoControle
from controles.zoeira import ZoeiraControle
from service.zoreira_service import ZoeiraService
import random


class Controle:
    command = ...  # type: str

    def __init__(self, msg):
        self.objeto = ZoeiraControle()
        self.msg = msg
        self.chat_id = msg['chat']['id']
        self.command = msg['text'].lower() or None

    def comando(self):
        dados = self.command.split()[1:]
        comando = self.command.split()[0]
        dados.insert(0, self.msg['from']['first_name'])
############################
        if comando in ["/d", "/dice", "/dado", "/d20", "/roll", "/r"]:
            objeto = DadoControle()
            try:
                return objeto.rolarDado(dados)
            except:
                return 'Erro de escrita, tente: 2d20+1.\n (quantidade: 2, dado: 20 faces, bonus: 1)'


'''
        elif self.busca_comando(["jogo", "jogar", "cs", "rb6", "lolzim", "lol"]) :
            self.objeto = ZoeiraControle()
            return self.objeto.jogo()


        elif self.busca_comando(["teco",
                                 "jadson",
                                 "big",
                                 "owl",
                                 "corujão",
                                 "douglas",
                                 ":owl:"]):
            self.objeto = ZoeiraControle()
            return self.objeto.teco()
        elif self.busca_comando(["gg",
                                 "win",
                                 "champs"]):
            self.objeto = ZoeiraControle()
            return self.objeto.feliz()
        elif self.busca_comando(["carreguei",
                                 "Disney",
                                 "carrega",
                                 "mochila",
                                 "mochilinha ",
                                 "rage",
                                 "quit",
                                 "troll",
                                 "trollitos",
                                 "trol",
                                 "fundo",
                                 "afundou",
                                 "afundando"]):
            self.objeto = ZoeiraControle()
            return self.objeto.rage()
'''
        elif busca_comando(self.busca_chaves()):
            return

        elif random.randint(0, 1):
            if "douglas" in self.msg['from']['first_name'].lower():
                return self.objeto.douglas()

            elif "carlos" in self.msg['from']['first_name'].lower():
                return self.objeto.carlos()

            elif "yan" in self.msg['from']['first_name'].lower():
                return self.objeto.yan()

            elif "jadson" in self.msg['from']['first_name'].lower():
                return self.msg['text'] or "Gênio!"

            elif "harã" in self.msg['from']['first_name'].lower():
                return self.objeto.hara()

            elif "marcos" in self.msg['from']['first_name'].lower():
                return self.objeto.marcos()


    def busca_comando(self, palavras):
        for p in palavras:
            if p in self.command:
                return True
        return False

    def busca_chaves(self):
       return  ZoeiraService.chaves()
    
    def busca_resposta(self,chave):
        respostas = ZoeiraService.respostas(chave)
        return respostas[random.randint(0, len(respostas)-1)]
        
    def retorna(self, ret):
        return ret

