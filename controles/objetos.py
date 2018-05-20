from models import Objetos, Personagem
import random
class ObjetosControle():
    def cria(self,dados):
        try:
            nome = dados[1] 
            dificuldade = int(dados[2])
            descricao = ' '.join(map(str,dados[3:]))
        except:
            return "Erro, tente: /criacenario Nome Dificuldade(1 a 20) descrição "
        try:
            cenario = Objetos.create(
            nome=nome,
            dificuldade=dificuldade,
            descricao=descricao
        )
        except :
            return "erro ao criar Objeto"
        return cenario.nome+": "+cenario.descricao

    def interage(self, dados):
        # 0         1           2       3
        #/interagir Personagem Objeto Ação
        try:
            objeto = Objetos.get(Objetos.nome == dados[2])
        except :
            return "Objeto não existe, tente: /interagir Personagem Objeto Ação"
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem não existe, tente: /interagir Personagem Objeto Ação" 
        for i in personagem.agilidade():
            if random.randint(1,20) > objeto.dificuldade:
                return personagem.nome+" conseguiu "+dados[3]+" com "+objeto.nome
        return personagem.nome+" Falhou em "+dados[3]+" com "+objeto.nome