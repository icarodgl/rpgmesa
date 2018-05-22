#!/usr/bin/python
# -*- coding: utf-8 -*-
from peewee import Model, CharField, IntegerField, ForeignKeyField, TextField, SqliteDatabase, PostgresqlDatabase
#db = SqliteDatabase('banco.db')
db = PostgresqlDatabase(
    'pfjbzmar',  # Required by Peewee.
    user='pfjbzmar',  # Will be passed directly to psycopg2.
    password='BD_RPGMESA',  # Ditto.
    host='tantor.db.elephantsql.com')  # Ditto.
'''
Itens dos personagens
'''
class Item(Model):
    nome = CharField()
    ataque = IntegerField(default=0)
    defesa = IntegerField(default=0)
    class Meta:
        database = db
'''
personagens
'''
class Personagem(Model):
    #dono do personagem
    usuario = CharField(null=True)
    #personagem
    nome = CharField()
    classe = CharField()
    nivel = IntegerField(default=1)
    vida= IntegerField(default=10)
    #atributos
    forca = IntegerField()
    inteligencia = IntegerField()
    resiliencia = IntegerField()
    destreza = IntegerField()
    agilidade = IntegerField()

    #itens
    cabeca = ForeignKeyField(Item,null=True)
    bra_dir = ForeignKeyField(Item,null=True)
    bra_esq = ForeignKeyField(Item,null=True)
    perna = ForeignKeyField(Item,null=True)
    peito = ForeignKeyField(Item,null=True)
    sapato = ForeignKeyField(Item,null=True)
    class Meta:
        database = db
'''
inventario dos personagens
'''


class Inventario(Model):
    item = ForeignKeyField(Item)
    personagem = ForeignKeyField(Personagem)
    class Meta:
        database = db
'''
figurantes ou monstros
'''
class Npc(Model):
    nome = CharField()
    classe = CharField()
    vida= IntegerField(default=10)
    nivel = IntegerField(default=1)
    #atributos
    forca = IntegerField()
    inteligencia = IntegerField()
    resiliencia = IntegerField()
    destreza = IntegerField()
    agilidade = IntegerField()
    class Meta:
        database = db

'''
tudo que esta no chao
'''
class Drop(Model):
    item = ForeignKeyField(Item)
    class Meta:
        database = db
'''
Objetos do jogo para interagir
'''
class Objetos(Model):
    nome = CharField()
    dificuldade = IntegerField(default=1)
    descricao = TextField()     
    class Meta:
        database = db
'''
cenários.
'''
class Cenario(Model):
    nome = CharField()
    descricao = TextField()
    class Meta:
        database = db
