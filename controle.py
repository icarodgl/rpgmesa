from controles.personagem import PersonagemControle
class Controle(object):
    def __init__(self,bot):
        self.bot = bot
        self.chat_id = any
        self.command = any

    def comando(self, msg):
        self.chat_id = msg['chat']['id']
        self.command = msg['text']
        dados = self.command.split()
        if "/criapersonagem" in self.command:
            self.criaPersonagem(dados)
        elif "/crianpc" in self.command:
            pass
        elif "/criacenario" in self.command:
            pass
        elif "/ataque" in self.command:
            pass


    def criaPersonagem(self,dados):
        # /cria classe nome
        personagem = PersonagemControle()
        personagem = personagem.cria(dados)
        self.bot.sendMessage(self.chat_id, "criado: "+str(personagem.nome)+str(personagem.classe))