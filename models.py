from peewee import *

db = SqliteDatabase('banco.db')
class Item(Model):

    nome = CharField()
    ataque = IntegerField()
    defesa = IntegerField()
    class Meta:
        database = db
class Personagem(Model):

    nome = CharField()
    classe = CharField()
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

class Inventario(Model):
    item = ForeignKeyField(Item)
    personagem = ForeignKeyField(Personagem)
    class Meta:
        database = db

class Npc(Model):
    nome = CharField()
    classe = CharField()
    nivel = IntegerField(default=1)
    #atributos
    forca = IntegerField()
    inteligencia = IntegerField()
    resiliencia = IntegerField()
    destreza = IntegerField()
    agilidade = IntegerField()
    class Meta:
        database = db

class Cenario(Model):
    nome = CharField()
    descricao = TextField()
    class Meta:
        database = db