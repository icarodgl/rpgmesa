#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import Drop, Personagem, Item, Inventario
from controles.mestre import MestreControle
import peewee
class DropControle ():
    def criaDrop(self,dado):
        if not MestreControle.mestre(dado[0]):
            return "Você não é mestre"

        #/drop item ataque defesa
        try:
            nome = dado[1]
            ataque = int(dado[2])
            defesa = int(dado[3])
        except:
            return "Erro nos dados, /drop nome_do_item Dano Defesa"
        try:
            item = Item()
            item  = item.create(
               nome=nome,
               ataque=ataque,
               defesa=defesa
           )
        except:
            return "erro ao criar item"
        try:
           drop = Drop()
           drop.create(
               item = item.id
           )
        except:
            return "Erro ao dropar"
        return item.nome+" Atk: "+str(item.ataque)+" Def: "+str(item.defesa)
    def pegaDrop(self,dado):
        #/pega Item
              
        pego = None
        drops = []
        drop = any 
        try:
            item = dado[1]
        except :
            return "Esqueceu o item a ser pego"
        try:
            drops = Drop.select(Drop, Item).join(Item)
        except:
            return "erro ao listar Drops"
        if len(drops)>0:
            for i in drops:
                if i.item.nome == item:
                    pego = i.item
                    drop = i
            if pego is None:
                return "%s não está no drop." %(item)
        else:
            return "não tem drop"
        try:
            per = Personagem.get(Personagem.usuario == dado[0])
        except:
            return "%s não possui um personagem"%(dado[0])
        
        try:
            inv = Inventario()
            inv.create(
            item = pego,
            personagem = per
            )
        except:
            return "Erro ao pegar item :("
        drop.delete_instance()
        return "%s pegou %s [ATK: %d / DEF: %d ] do drop" %(per.nome,pego.nome,pego.ataque, pego.defesa )
    def limpaDrop(self):
        try:
            objetos = Drop.select()
        except:
            return "erro ao listar Drops"
        for o in objetos:
            o.delete_instance()
        return "Limpo! ;)"
    def listaDrop(self):
        try:
            drops = Drop.select()
        except:
            return "erro ao listar Drops"
        frase = "Drops:\n" 
        for d in drops:
            item = d.item
            frase += " - %s [ATK: %d / DEF: %d ]\n"%(item.nome,item.ataque,item.defesa)
        return frase