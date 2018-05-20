from random import *
from models import Personagem, Item
class Controle(object):

    def __init__(self,bot):
        self.bot = bot
        self.chat_id = any
        self.command = any
    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text']
        if "/cria" in self.command:
            self.cria()
    def cria(self):

        # .cria classe nome
        r = self.command.split()
        classe = ""
        nome = r[2]
        forca = randint(1,10)
        inteligencia = randint(1,10)
        resiliencia = randint(1,10)
        destreza = randint(1,10)
        agilidade = randint(1,10)
        if "guerreiro" in self.command :
            classe = "guerreiro"
            mao1 = Item.create(nome="espada",ataque=5,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=2)
            peito = Item.create(nome="malha",ataque=0,defesa=5)
            perna = Item.create(nome="malha",ataque=0,defesa=2)

        elif "mago" in self.command:
            classe ="mago"
            mao1 = Item.create(nome="cajado",ataque=10,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=1)
        elif "clerigo" in self.command:
            classe = "clerigo"  
            mao1 = Item.create(nome="livro",ataque=10,defesa=1)
            mao2 = Item.create(nome="escudo",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=2)
        else:
            classe = "nenhum"  
            mao1 = Item.create(nome="graveto",ataque=1,defesa=1)
            mao2 = Item.create(nome="tabua",ataque=0,defesa=1)
            peito = Item.create(nome="manto",ataque=0,defesa=2)
            perna = Item.create(nome="tanga",ataque=0,defesa=2)

        cabeca = Item.create(nome="cabeça",ataque=0,defesa=0)
        sapato = Item.create(nome="sapato",ataque=0,defesa=0)
        personagem = Personagem.create(
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
        self.bot.sendMessage(self.chat_id, "criado: "+str(personagem.nome))