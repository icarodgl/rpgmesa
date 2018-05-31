#!/usr/bin/python3
# -*- coding: utf-8 -*-
from peewee import Model, CharField, IntegerField, ForeignKeyField, TextField
from banco import BancoConfig

db = BancoConfig.banco()

'''
ModeloBase das classes
'''


class ModeloBase(Model):
    def __str__(self):
        return str(self)

    class Meta:
        database = db

'''
Itens dos personagens
'''
class Item(ModeloBase):
    nome = CharField()
    ataque = IntegerField(default=0)
    defesa = IntegerField(default=0)


class Mestre(ModeloBase):
    usuario = CharField(null=True)

'''
personagens
'''
class Personagem(ModeloBase):
    #dono do personagem
    usuario = CharField(null=True)
    #personagem
    nome = CharField()
    classe = CharField()
    nivel = IntegerField(default=1)
    vidamax = IntegerField(default=50)
    pontos = IntegerField(default=0)
    vida= IntegerField(default=10)
    #atributos
    forca = IntegerField()
    inteligencia = IntegerField()
    resiliencia = IntegerField()
    destreza = IntegerField()
    agilidade = IntegerField()

    #itens
    cabeca = ForeignKeyField(Item,null=True,backref="cabeca")
    bra_dir = ForeignKeyField(Item,null=True,backref="bra_dir")
    bra_esq = ForeignKeyField(Item,null=True,backref="bra_esq")
    perna = ForeignKeyField(Item,null=True,backref="perna")
    peito = ForeignKeyField(Item,null=True,backref="peito")
    sapato = ForeignKeyField(Item,null=True,backref="sapato")

'''
inventario dos personagens
'''


class Inventario(ModeloBase):
    item = ForeignKeyField(Item)
    personagem = ForeignKeyField(Personagem)

'''
figurantes ou monstros
'''
class Npc(ModeloBase):
    nome = CharField()
    classe = CharField()
    vida = IntegerField(default=50)
    vidamax = IntegerField(default=50)
    nivel = IntegerField(default=1)
    #atributos
    forca = IntegerField()
    inteligencia = IntegerField()
    resiliencia = IntegerField()
    destreza = IntegerField()
    agilidade = IntegerField()


'''
tudo que esta no chao
'''
class Drop(ModeloBase):
    item = ForeignKeyField(Item)

'''
Objetos do jogo para interagir
'''
class Objetos(ModeloBase):
    nome = CharField()
    dificuldade = IntegerField(default=1)
    descricao = TextField()     

'''
cenários.
'''
class Cenario(ModeloBase):
    nome = CharField()
    descricao = TextField()

