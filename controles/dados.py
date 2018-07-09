#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import re

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
            "valor":[],
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
                dado['valor'].append( valor )
            ldado.append(dado)
        frase = self.textificar(ldado)
        frase = args[0]+' rolou:\n'+frase
        return frase

    def textificar(self,dados):
        frase = ''
        total = 0
        for elem in dados:
            frase += 'd%d: '%(elem['dado'])
            for i in range(len(elem['valor'])):
                total+=elem['valor'][i]
                frase += '(%d)'%(elem['valor'][i])
            if elem['bonus'] != 0:
                frase+= '\n Total: %d, +Bonus: %d \n'%(total, total+elem['bonus'])
                total = 0
            else:
                frase+= ' Total: %d \n'%(total)
                total = 0
        return frase
        