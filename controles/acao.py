from models import Personagem
import random
class AcaoControle():
    def roll(self):
        return "D20: "+str(random.randint(1,20))
    def dadoAgi(self, dados):
        personagem = self.getPersonagem(dados[2])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.agilidade)
        return personagem.nome+" conseguiu "+", ".join(map(str,d20))

    def dadoDex(self, dados):

        personagem = self.getPersonagem(dados[2])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.destreza)
        return personagem.nome+" conseguiu "+", ".join(map(str,d20))

    def dadoInt(self, dados):

        personagem = self.getPersonagem(dados[2])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.inteligencia)
        return personagem.nome+" conseguiu "+", ".join(map(str,d20))

    def dadoFor(self, dados):

        personagem = self.getPersonagem(dados[2])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.forca)
        return personagem.nome+" conseguiu "+", ".join(map(str,d20))

    def dadoRes(self, dados):

        personagem = self.getPersonagem(dados[2])
        if personagem is None:
            return "Personagem não encontrado"
        d20 = self.jogaD20(personagem.resiliencia)
        return personagem.nome+" conseguiu "+", ".join(map(str,d20))

    def getPersonagem(self, nome):
        try:
            return Personagem.get(Personagem.nome == nome)
        except :
            return None

    def jogaD20(self,quantidade):
        d20 = []
        for i in range(quantidade):
            d20.append(random.randint(1,20))
        return d20
        