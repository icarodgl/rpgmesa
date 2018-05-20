from peewee import *
from models import *
## configurações do banco
db = SqliteDatabase('banco.db')
criar_tabelas = True

modelos = [
            Personagem,
            Item,
            Inventario,
            Npc,
            Cenario
            ]

if (criar_tabelas):
    db.connect()
    db.create_tables(modelos)