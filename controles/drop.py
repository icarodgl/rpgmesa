from models import Drop, Personagem, Item, Inventario
import peewee
class DropControle ():
    def criaDrop(self,dado):
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
        #/pega personagem Item
        if len(dado) < 2:
            return "Erro, tente: /pega personagem Item"
        
        pego = None
        drops = []
        drop = any 
        try:
            drops = Drop.select(Drop, Item).join(Item)
        except:
            return "erro ao listar Drops"
        if len(drops)>0:
            for i in drops:
                if i.item.nome == dado[2]:
                    pego = i.item
                    drop = i
            if pego is None:
                return "item não está no drop: "+dado[2]
        else:
            return "não tem drop"
        try:
            per = Personagem.get(Personagem.nome == dado[1])
        except:
            return "Personagem não encontrado"
        
        try:
            inv = Inventario()
            inv.create(
            item = pego,
            personagem = per
            )
        except:
            return "erro ao criar inventario"
        drop.delete_instance()
        return per.nome+" Pegou "+pego.nome

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
        frase = "Drops:" 
        for d in drops:
            item = d.item
            frase += " "+item.nome+"(Atk: "+str(item.ataque)+" /Def: "+str(item.defesa)+")"
        return frase