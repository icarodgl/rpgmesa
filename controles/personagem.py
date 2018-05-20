from random import *
from models import Personagem, Item
class PersonagemControle():
    def cria(self, dados):
        classe = ""
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