from models import Objetos, Personagem
import random
class ObjetosControle():
    def cria(self,dados):
        try:
            nome = dados[1] 
            dificuldade = int(dados[2])
            descricao = ' '.join(map(str,dados[3:]))
        except:
            return "Erro, tente: /criaobjeto Nome Dificuldade(1 a 20) descrição "
        try:
            objeto = Objetos.create(
            nome=nome,
            dificuldade=dificuldade,
            descricao=descricao
        )
        except :
            return "erro ao criar Objeto"
        return objeto.nome+": "+objeto.descricao+" dificuldade: "+str(objeto.dificuldade)

    def interage(self, dados):
        # 0         1           1:len(dados-2)       :len(dados-1)
        #/interagir Personagem ação objeto
        erro = " não existe, tente: /interagir Personagem Ação Objeto"
        try:
            objeto = Objetos.get(Objetos.nome == dados[len(dados)-1:])
        except :
            return "Objeto"+erro
        try:
            personagem = Personagem.get(Personagem.nome == dados[1])
        except :
            return "Personagem"+erro
        d20 = random.randint(1,20)
        frase = ""
        if d20 >= objeto.dificuldade:
            frase =  personagem.nome+" "+" ".join(dados[2:len(dados)-1])+" "+objeto.nome+" com sucesso! ("+str(d20)+"/"+str(objeto.dificuldade)+")"
        frase =  personagem.nome+" Não "+" ".join(dados[2:len(dados)-1])+" "+objeto.nome+" ("+str(d20)+"/"+str(objeto.dificuldade)+")"
        objeto.delete_instance()
        return frase
    def listaObjetos(self):
        try:
            objetos = Objetos.select()
        except:
            return "erro ao listar objetos"
        frase = "Objetos:" 
        for o in objetos:
            frase += " "+o.nome+"("+str(o.dificuldade)+")"
        return frase
    def limpaObjetos(self):
        try:
            objetos = Objetos.select()
        except:
            return "erro ao listar objetos"
        for o in objetos:
            o.delete_instance()
        return "Limpo! ;)"