from peewee import *

db = SqliteDatabase('banco.db')
class Item(Model):

    nome = CharField()
    
    ataque = IntegerField()
    defesa = IntegerField()


    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente.
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
    cabeca = ForeignKeyField(Item)
    bra_dir = ForeignKeyField(Item)
    bra_esq = ForeignKeyField(Item)
    perna = ForeignKeyField(Item)
    peito = ForeignKeyField(Item)
    sapato = ForeignKeyField(Item)
      
    class Meta:
        # Indica em qual banco de dados a tabela
        # 'author' sera criada (obrigatorio). Neste caso,
        # utilizamos o banco 'codigo_avulso.db' criado anteriormente.
        database = db

