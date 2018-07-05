#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import re
import copy
class DadoControle():

    def rolarDado(args):
        dados = args[1:]
        ldado = []
        for elem in dados:
            dado = {
            "dado":int,
            "valor":0,
            "bonus":0
            }
            dx = (elem.split('d'))
            if dx[0] == '':
                dx.pop(0)
            if len(dx) > 1:
                quant = int(dx[0])
            else:
                quant = 1
            if (len(elem.split('-')) > 1 ):
                dado['bonus'] = int((elem.split('-'))[-1])*-1
                dado['dado'] = int(re.split(' *, *',(elem.split('-')[-2].split('d')[-1]))[0])
            elif (len(elem.split('+')) > 1 ):
                dado['bonus'] = int(elem.split('+')[-1])
                dado['dado'] = int(re.split(' *, *',(elem.split('+')[-2].split('d')[-1]))[0])
            else:
                dado['dado'] = int(dx[-1])
            for q in range(quant):
                valor = random.randint(1,dado['dado'])
                if dado['bonus'] > 0:
                    valor += dado['bonus']
                dado['valor'] = valor
                ldado.append(copy.copy(dado))

        frase = self.textificar(ldado)
        frase = dados[0]+frase
        return frase

    def textificar(dados):
        frase = ''
        
        for elem in dados:
            frase += 'dado: %d, valor: %d, bonus:%d \n' %(elem['dado'],elem['valor'],elem['bonus'])
        return frase
        