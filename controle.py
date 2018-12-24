#!/usr/bin/python3
# -*- coding: utf-8 -*-
from emoji import emojize
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from controles.dados import DadoControle
from controles.zoeira import ZoeiraControle


class Controle(object):
    def __init__(self, bot):
        self.bot = bot
        self.chat_id = any
        self.command = any
        self.objeto = any

    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text'].lower()
        dados = self.command.split()
        comando = self.command.split()[0]
        dados = dados[1:]
        dados.insert(0, msg['from']['first_name'] +
                     " " + msg['from']["last_name"])
        if comando in ["/d", "/dice", "/dado", "/d20", "/roll", "/r"]:
            self.objeto = DadoControle()
            try:
                ret = self.objeto.rolarDado(dados)
                self.retorna(ret)
            except:
                self.retorna(
                    'Erro de escrita, tente: 2d20+1.\n (quantidade: 2, dado: 20 faces, bonus: 1)')

        elif comando in ["/teco", "/jadson"]:
            self.objeto = ZoeiraControle()
            ret = self.objeto.teco()
            self.retorna(ret)
        elif comando in ["/hara", "/harã"]:
            self.objeto = ZoeiraControle()
            ret = self.objeto.hara()
            self.retorna(ret)
        elif comando in ["/doug", "/douglas", "/bw"]:
            self.objeto = ZoeiraControle()
            ret = self.objeto.doug()
            self.retorna(ret)
        elif comando in ["/stick"]:
            self.objeto = ZoeiraControle()
            ret = self.objeto.pegaStickAleatorio()
            self.retornaStick(ret)
        elif comando in ["/salvastick"]:
            self.objeto = ZoeiraControle()
            ret = self.objeto.salvaStick(dados)
            self.retornaStick(ret)
        else:
            self.retornaStick("CAADBAADpgADWSJOBYvDjrzJBxB_Ag")
            ## self.retorna('Comando não cadastrado')

    def retorna(self, ret):
        self.bot.sendMessage(self.chat_id, emojize("%s" %
                                                   ret, use_aliases=True))

    def retornaStick(self, stickId):
        self.bot.sendSticker(self.chat_id, stickId)

    def teclado(self, dados):
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Personagem', callback_data="/ajuda"),
            InlineKeyboardButton(text='Mestre', callback_data="/ajudam"),
        ]])
        self.bot.sendMessage(self.chat_id,
                             text="Ajuda:",
                             reply_markup=keyboard)
