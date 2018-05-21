#!/usr/bin/python
# -*- coding: utf-8 -*-
from peewee import *
from models import *
## configura do banco
#db = SqliteDatabase('banco.db')
db = PostgresqlDatabase(
    'pfjbzmar',  # Required by Peewee.
    user='pfjbzmar',  # Will be passed directly to psycopg2.
    password='e3vvH5pZZH_rdqfIBj7NFrW4hnS7n31C',  # Ditto.
    host='tantor.db.elephantsql.com')  # Ditto.
criar_tabelas = True

modelos = [
            Personagem,
            Item,
            Inventario,
            Npc,
            Cenario,
            Objetos,
            Drop
            ]

if (criar_tabelas):
    db.connect()
    db.create_tables(modelos)