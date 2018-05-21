#!/usr/bin/python
# -*- coding: utf-8 -*-
from peewee import *
from models import *
## configura do banco
db = SqliteDatabase('banco.db')
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