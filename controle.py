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
        self.chave = ""

    def comando(self):
        dados = self.command.split()[1:]
        comando = self.command.split()[0]
        dados.insert(0, self.msg['from']['first_name'])
        self.chave = self.busca_comando(self.busca_chaves())
############################
        if comando in ["/d", "/dice", "/dado", "/d20", "/roll", "/r"]:
            objeto = DadoControle()
            try:
                return objeto.rolarDado(dados)
            except:
                return 'Erro de escrita, tente: 2d20+1.\n (quantidade: 2, dado: 20 faces, bonus: 1)'

        elif self.chave != "":
            if self.chave == 'Erro':
                return 'Erro'
            return self.busca_resposta(self.chave)

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
            if p.lower() in self.command:
                return p
        return ""

    def busca_chaves(self):
        chave = ZoeiraService()
        return chave.chaves()
    
    def busca_resposta(self,chave):
        z = ZoeiraService()
        respostas = z.respostas(chave)
        r = respostas['respostas']
        return r[random.randint(0, len(r)-1)]

    def retorna(self, ret):
        return ret

