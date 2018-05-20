from peewee import *
from models import *
## configurações do banco
db = SqliteDatabase('banco.db')
criar_tabelas = True

if (criar_tabelas):
    db.connect()
    db.create_tables([Personagem, Item])