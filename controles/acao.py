from models import Personagem
import random
class AcaoControle():
    def interage(self, dados):
        # 0         1      2
        #/acao Personagem Ação
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem não existe, tente: /acao Personagem Ação" 
        d20 = []
        for i in personagem.agilidade():
            d20.append(random.randint(1,20))
        print(personagem.nome+" conseguiu "+" ".join(map(str,d20)))
        return personagem.nome+" conseguiu "+" ".join(map(str,d20))
