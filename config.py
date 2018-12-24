#!/usr/bin/python
# -*- coding: utf-8 -*-

from models import Personagem, Inventario, Item, Npc, Cenario, Objetos, Drop, Mestre, MyStick
from banco import BancoConfig

modelos = [
    Personagem,
    Item,
    Inventario,
    Npc,
    Cenario,
    Objetos,
    Drop,
    Mestre,
    MyStick
]

if True:  # true para criar banco
    db = BancoConfig.banco()
    db.connect()
    if True:  # True para Limpar banco
        db.drop_tables(modelos)
    db.create_tables(modelos)
    db.close()
