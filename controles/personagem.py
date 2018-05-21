from random import *
from models import Personagem, Item, Inventario, Drop
class PersonagemControle():
    def cria(self, dados):
        classe = [""]
        try:
            nome = dados[1]
            usuario = dados[0]
        except:
            return "Erro, tente : /criapersonagem Nome Classe"

        forca = randint(1,10)
        inteligencia = randint(1,10)
        resiliencia = randint(1,10)
        destreza = randint(1,10)
        agilidade = randint(1,10)
        if "guerreiro" in dados :
            classe = "guerreiro"
            mao1 = Item.create(nome="espada",ataque=5,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=2)
            peito = Item.create(nome="malha",ataque=0,defesa=5)
            perna = Item.create(nome="malha",ataque=0,defesa=2)

        elif "mago" in dados:
            classe ="mago"
            mao1 = Item.create(nome="cajado",ataque=10,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=1)
        elif "clérigo" in dados:
            classe = "clerigo"  
            mao1 = Item.create(nome="livro",ataque=10,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=2)
        else:
            classe = "nenhuma"  
            mao1 = Item.create(nome="graveto",ataque=5,defesa=5)
            mao2 = Item.create(nome="tabua",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=2)

        cabeca = Item.create(nome="cabeça",ataque=0,defesa=0)
        sapato = Item.create(nome="sapato",ataque=0,defesa=0)
        try:
            personagem = Personagem.create(
                        usuario=usuario,
                        nome=nome,
                        classe=classe,
                        cabeca=cabeca,
                        bra_dir=mao1,
                        bra_esq=mao2,
                        peito=peito,
                        perna=perna,
                        sapato=sapato,
                        forca=forca,
                        inteligencia=inteligencia,
                        resiliencia=resiliencia,
                        destreza=destreza,
                        agilidade=agilidade
                        )
        except:
            return "Erro ao criar personagem"
        return "criado: "+str(personagem.nome)+" : "+str(personagem.classe)

    def levelup(self,dados):
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem não encontrado"

        classe = personagem.classe
        personagem.nivel +=1
        personagem.forca +=1
        personagem.inteligencia +=1
        personagem.agilidade +=1
        personagem.destreza+=1
        personagem.resiliencia+=1

        if classe == "guerreiro":
            personagem.forca +=2
            personagem.resiliencia+=2
        elif classe == "clerigo":
            personagem.resiliencia+=2
            personagem.inteligencia +=2
        elif classe == "mago":
            personagem.inteligencia +=3
            personagem.destreza+=1
        
        personagem.vida = 10*personagem.resiliencia 
        personagem.save()
        return personagem.nome+" nivel: "+str(personagem.nivel)
    def ficha(self,dados):
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem não encontrado"

        return "Ficha: "+personagem.nome+" Vida: "+str(personagem.vida)+"\n Classe: "+personagem.classe+" Nivel: "+str(personagem.nivel)+"\n for: "+str(personagem.forca)+"\n agi: "+str(personagem.agilidade)+"\n des: "+str(personagem.destreza)+"\n int: "+str(personagem.inteligencia)+"\n res: "+str(personagem.resiliencia)

    def equipamentos(self,dados):
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem não encontrado"
        equips={}
        equips["bra_dir"] = (Item.get_by_id(personagem.bra_dir))
        equips["bra_esq"] = (Item.get_by_id(personagem.bra_esq))
        equips["peito"] = (Item.get_by_id(personagem.peito))
        equips["perna"] = (Item.get_by_id(personagem.perna))
        equips["sapato"] = (Item.get_by_id(personagem.sapato))
        equips["cabeca"] = (Item.get_by_id(personagem.cabeca))
        palavra = "Equipamentos: \n"
        for i in equips:
            palavra+=str(equips[i].nome)+" A: "+str(equips[i].ataque)+" D: "+str(equips[i].defesa)+"\n"
        return palavra

    def inventario(self,dado):
        #/saco personagem
        saco = []
        try:
            pe = Personagem.get(Personagem.nome == dado[1])
        except:
            return "Personagem não encontrado"
        try:
            inventario = Inventario.select().where("personagem_id" == pe.id)
            for i in inventario:
                print(i.nome)
        except :
            return "Erro ao listar itens"
        frase = pe.nome+" Itens:"
        for i in saco:
            frase+= " "+i.nome+" (A: "+i.ataque+"/D: "+i.defesa+")"
        return frase