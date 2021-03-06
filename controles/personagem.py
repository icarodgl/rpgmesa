#!/usr/bin/python
# -*- coding: utf-8 -*-
from random import *
from models import Personagem, Item, Inventario
from peewee import *
from controles.mestre import MestreControle


class PersonagemControle():

    @staticmethod
    def equipamentos(dados):
        usuario = dados[0]
        try:
            person = Personagem.get(Personagem.usuario == usuario)
        except:
            return "Você não possui personagem cadastrado :disappointed:"
        try:
            lista = [Item.get_by_id(person.cabeca), Item.get_by_id(person.bra_dir), Item.get_by_id(person.bra_esq),
                     Item.get_by_id(person.peito), Item.get_by_id(person.perna), Item.get_by_id(person.sapato)]
        except:
            return "Erro ao listar seus itens :disappointed:"
        frase = "Equipamentos: \n"
        nomes = ["cabeça", "direita", "esquerda", "peito", "calça", "sapato"]
        for i in range(len(lista)):
            frase += " - %s => %s [ATK: %d , DEF: %d]\n" % (
                nomes[i], lista[i].nome, lista[i].ataque, lista[i].defesa)
        return frase

    @staticmethod
    def cria(dados):
        """

        :type dados: list
        """
        try:
            pe = Personagem.get(Personagem.usuario == dados[0])
        except:
            try:
                nome = dados[1]
                usuario = dados[0]
                classe = dados[2]
            except:
                return "Erro, tente : /criapersonagem Nome Classe"

            forca = randint(5, 20)
            inteligencia = randint(5, 20)
            resiliencia = randint(10, 20)
            destreza = randint(5, 20)
            agilidade = randint(5, 20)
            vida = resiliencia * 10
            mao1 = Item.create(nome="graveto", ataque=5, defesa=0)
            mao2 = Item.create(nome="tabua", ataque=0, defesa=5)
            peito = Item.create(nome="Camisa_rasgada", ataque=0, defesa=2)
            perna = Item.create(nome="tanga", ataque=0, defesa=2)
            cabeca = Item.create(nome="cabeça", ataque=0, defesa=0)
            sapato = Item.create(nome="sapato", ataque=0, defesa=1)

            try:
                personagem = Personagem.create(
                    vida=vida,
                    vidamax=vida,
                    usuario=usuario,
                    nome=nome,
                    classe=classe,
                    cabeca=cabeca,
                    bra_dir=mao1,
                    bra_esq=mao2,
                    peito=peito,
                    perna=perna,
                    sapato=sapato,
                    forca=forca,
                    inteligencia=inteligencia,
                    resiliencia=resiliencia,
                    destreza=destreza,
                    agilidade=agilidade
                )
            except:
                return "Erro ao criar personagem"
            return "criado: %s classe: %s " % (personagem.nome, personagem.classe)
        return "Você possui já um personagem: %s " % pe.nome

    def dormir(self, dados):
        try:
            personagem = Personagem.get(
                Personagem.usuario == dados[0])  # type: Personagem
        except:
            return "Personagem não encontrado"
        personagem.vida = personagem.vidamax
        personagem.save()
        return "%s Vida: [%d / %d ] :heart:" % (
            personagem.nome, personagem.vida, personagem.vidamax)

    def levelup(self, dados):
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre :kissing_heart:"
        try:
            personagem = Personagem.get(
                Personagem.nome == dados[1])  # type: Personagem
        except:
            return "Personagem não encontrado"
        personagem.pontos += 5
        personagem.vida = personagem.vidamax
        personagem.nivel += 1
        personagem.save()
        return "%s nivel: %d possui: %d pontos não distibuidos" % (
            personagem.nome, personagem.nivel, personagem.pontos)

    def deletarPersonagem(self, dados):
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre :kissing_heart:"
        try:
            personagem = Personagem.get(
                Personagem.nome == dados[1])  # type: Personagem
        except:
            return "Personagem não encontrado"
        personagem.delete_instance()
        return "%s Desapareceu do mapa " % (personagem.nome)

    def darPontos(self, dados):
        # /doar personagem quantidade
        if not MestreControle.mestre(dados[0]):
            return "Você não é mestre :kissing_heart:"
        try:
            quantidade = int(dados[2])
        except:
            return "Errp, tente: /doar personagem quantidade"
        try:
            personagem = Personagem.get(
                Personagem.nome == dados[1])  # type: Personagem
        except:
            return "Personagem não encontrado"
        personagem.pontos += quantidade
        personagem.save()
        return "%s, %d possui: %d pontos não distibuidos" % (
            personagem.nome, personagem.pontos)

    def addatributo(self, dados):
        # /add atributo quantidade
        try:
            usuario = dados[0]
            atributo = dados[1]
            quantidade = int(dados[2])
        except:
            return "Erro faltando dados: /add atributo quantidade"
        try:
            personagem = Personagem.get(Personagem.usuario == usuario)
        except:
            return "Personagem não encontrado"
        emoji = ""
        if personagem.pontos < quantidade:
            return "Você possui %d pontos" % personagem.pontos
        x = atributo[0].lower()
        if x == "a":
            emoji = " :running:"
            personagem.agilidade += quantidade
        elif x == "d":
            emoji = "  :dart:"
            personagem.destreza += quantidade
        elif x == "f":
            emoji = " :muscle:"
            personagem.forca += quantidade
        elif x == "i":
            emoji = " :mortar_board:"
            personagem.inteligencia += quantidade
        elif x == "r":
            emoji = " :beginner: :heart:"
            personagem.resiliencia += quantidade
            personagem.vidamax = personagem.resiliencia * 10
            personagem.vida = personagem.vidamax
        else:
            return "Não existe atributo: %s ,tente: (agi,des,for,int,res)" % atributo
        personagem.pontos -= quantidade
        personagem.save()
        return "%s adicionou %d em %s %s.\n restam %d pontos" % (personagem.nome, quantidade, atributo, emoji, personagem.pontos)

    def ficha(self, dados):
        try:
            personagem = Personagem.get(Personagem.usuario == dados[0])
        except:
            return "Você não possui personagem"

        return "Ficha: " + personagem.nome + " Vida : " + str(
            personagem.vida) + "\n Classe: " + personagem.classe + " Nivel: " + str(
            personagem.nivel) + "\n for: " + str(personagem.forca) + "\n agi: " + str(
            personagem.agilidade) + "\n des: " + str(personagem.destreza) + "\n int: " + str(
            personagem.inteligencia) + "\n res: " + str(personagem.resiliencia
                                                        ) + "\n Pontos não distribuidos: " + str(personagem.pontos)

    def inventario(self, dado):
        # /saco
        saco = []
        try:
            pe = Personagem.get(Personagem.usuario == dado[0])
        except:
            return "%s não possui personagem cadastrado" % (dado[0])
        try:
            query = (Item
                     .select()
                     .join(Inventario)
                     .join(Personagem)
                     .where(Personagem.nome == pe.nome))
            for item in query:
                saco.append(item)
        except:
            return "Erro ao listar itens"
        frase = " Itens de %s:\n" % (pe.nome)
        for i in saco:
            frase += " - %s [ATK: %d / DEF: %d ]\n" % (
                i.nome, i.ataque, i.defesa)
        return frase

    def equipar(self, dado):
        # /equipar item local
        saco = []
        inventario = Inventario
        try:
            equipamento = dado[1]
            posicao = dado[2]
            usuario = dado[0]
        except:
            return "Erro, tente:\n /equipar item posição: \n :skull: cabeça \n :jeans: perna\n :mans_shoe: pé\n :shirt: peito\n :point_right: direita \n :point_left: esquerda"
        try:
            pe = Personagem.get(Personagem.usuario == usuario)
        except:
            return "%s não possui personagem cadastrado :kissing_heart:" % usuario

        try:
            '''pe.inventario = (Item
                     .select()
                     .join(Inventario)
                     .join(Personagem)
                     .where(Personagem.nome == pe.nome))'''

            pe.inventario = (Inventario
                             .select(Inventario, Personagem, Item)
                             .join(Personagem)
                             .switch(Inventario)
                             .join(Item))

        except:
            return "Erro ao listar itens"
        for i in pe.inventario:
            if equipamento == i.item.nome:
                segura = Item
                mod = ""
                if posicao in ["cabeça", "cabeca", "top", "capacete", "elmo", "1"]:
                    segura = pe.cabeca
                    mod = "cabeca"
                    pe.cabeca = i.item
                elif posicao in ["calça", "perna", "calca", "5"]:
                    segura = pe.perna
                    mod = "perna"
                    pe.perna = i.item
                elif posicao in ["peito", "armadura", "4"]:
                    segura = pe.peito
                    mod = "peito"
                    pe.peito = i.item
                elif posicao in ["pe", "sapato", "foot", "pé", "6"]:
                    segura = pe.sapato
                    mod = "sapato"
                    pe.sapato = i.item
                elif posicao in ["direito", "direita", "mão_direita", "mao_direita", "braço_direito", "2"]:
                    segura = pe.bra_dir
                    mod = "bra_dir"
                    pe.bra_dir = i.item
                elif posicao in ["esquerda", "esquerdo", "mao_esquerda", "braço_esquerdo", "mão_esquerda", "3"]:
                    segura = pe.bra_esq
                    mod = "bra_esq"
                    pe.bra_esq = i.item
                else:
                    return "Escolha uma posição para colocar %s: \n :skull: cabeça \n :jeans: perna\n :mans_shoe: pé\n :shirt: peito\n :point_right: direita \n :point_left: esquerda" % (dado[1])

                try:
                    i.item = segura
                    i.save()
                except IntegrityError:
                    return "Erro ao trocar itens :mask:"
                try:
                    pe.save()
                except IntegrityError:
                    return "Erro ao equipar itens :mask:"

                return "Equipado! :ok_hand:"
        return "Você não possui %s em seu inventario" % dado[1]
