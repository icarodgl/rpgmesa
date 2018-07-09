#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import re
import copy
class DadoControle():
    def rolarDado(self, args):
        if len(args) >1:
            dados = args[1:]
        else:
            dados = ['20']
        ldado = []
        for elem in dados:
            dado = {
            "quantidade":int,
            "dado":int,
            "valor":0,
            "bonus":0
            }
            dx = (elem.split('d'))
            if dx[0] == '':
                dx.pop(0)
            if len(dx) > 1:
                dado["quantidade"] = int(dx[0])
            else:
                dado["quantidade"] = 1
            if (len(elem.split('-')) > 1 ):
                dado['bonus'] = int((elem.split('-'))[-1])*-1
                dado['dado'] = int(re.split(' *, *',(elem.split('-')[-2].split('d')[-1]))[0])
            elif (len(elem.split('+')) > 1 ):
                dado['bonus'] = int(elem.split('+')[-1])
                dado['dado'] = int(re.split(' *, *',(elem.split('+')[-2].split('d')[-1]))[0])
            else:
                dado['dado'] = int(dx[-1])
            for q in range(dado["quantidade"]):
                valor = random.randint(1,dado['dado'])
                dado['valor'] += valor
                ldado.append(copy.copy(dado))
        frase = self.textificar(ldado)
        frase = args[0]+' rolou:\n'+frase
        return frase

    def textificar(self,dados):
        frase = ''
        total = 0
        for elem in dados:
            if elem['bonus'] != 0:
                frase += 'd%d: %d + %d = %d \n' %(elem['dado'],elem['valor'],elem['bonus'],elem['valor']+elem['bonus'])
            else:
                frase += 'd%d: %d\n' %(elem['dado'],elem['valor'])
            total += elem['valor']
        frase += 'Total: %d\n' %(total)
        return frase
        