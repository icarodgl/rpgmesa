#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import Objetos, Personagem
from controles.mestre import MestreControle
import random
class ObjetosControle():
    def cria(self,dados):
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre"

        try:
            nome = dados[1] 
            dificuldade = int(dados[2])
            descricao = ' '.join(map(str,dados[3:]))
        except:
            return "Erro, tente: /criaobjeto Nome Dificuldade(1 a 20) descrição "
        try:
            objeto = Objetos.create(
            nome=nome,
            dificuldade=dificuldade,
            descricao=descricao
        )
        except :
            return "erro ao criar Objeto"
        return objeto.nome+": "+objeto.descricao+" dificuldade: "+str(objeto.dificuldade)

    def interage(self, dados):
        # 0         1           1:len(dados-2)       :len(dados-1)
        #/interagir ação objeto
        erro = " não existe, tente: /ação jogar pedra"
        try :
            objeto = Objetos.get(Objetos.nome == dados[-1])
        except  :
            return "Objeto "+erro
        try:
            personagem = Personagem.get(Personagem.usuario == dados[0])
        except  :
            return "Personagem? "+erro
        d20 = random.randint(1,20)
        frase = ""
        if d20 > objeto.dificuldade:
            frase +=  "%s %s %s :+1:\n Tirou %d de %d" %(personagem.nome, " ".join(dados[1:-1]), objeto.nome, d20, objeto.dificuldade )
        else :
            frase +=  "%s não %s %s :-1:\n Tirou %d de %d" %(personagem.nome, " ".join(dados[1:-1]), objeto.nome, d20, objeto.dificuldade)
        objeto.delete_instance()
        return frase

    def listaObjetos(self):
        try:
            objetos = Objetos.select()
        except :
            return "erro ao listar objetos"
        frase = "Objetos: [Dificuldade] \'descrição\' \n" 
        for o in objetos:
            frase += "- %s : [%d/20] \'%s\'\n" %(o.nome,o.dificuldade, o.descricao)
        return frase

    def limpaObjetos(self, dados):

        try:
            objetos = Objetos.select()
        except :
            return "erro ao listar objetos"
        for o in objetos:
            o.delete_instance()
        return "Limpo! ;)"