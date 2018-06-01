class AjudaControle:
    def ajuda(self):
        ret = "/ficha - ver sua ficha\n"
        ret +="/pega faca - pegar itens\n"
        ret += "/drops -ver itens\n"
        ret += "/atacar Inimigo - ataca um personagem ou npc\n"
        ret += "/roll - rola um d20\n"
        ret += "/equipar faca - equipa um item do seu inventário\n"
        ret += "/i - ve seu inventario\n"
        ret += "/e ve seus itens equipados\n"
        ret += "/add força 5 - almenta o atributo\n"
        ret += "/lnpc - lista de npcs no jogo\n"
        ret +="/lobjetos - lista objetos para interagir\n"
        ret +="/ação jogar pedra - ação sobre um objeto\n"
        ret += "/dormir - descansar seu personagem.\n"
        ret += "/ajudam - Ajuda do mestre.\n"
        return ret

    def ajudaM(self):
        ret = "/crianpc nome 5 - cria npc com nivel 5\n"
        ret = "/criaobjeto pedra 5- cria objeto com dificuldade 5\n"
        ret = "/killall - mata todos os npcs\n"
        ret = "/dropar faca 10 1 - dropa faca com atk:10  def:1\n"
         ret = "/decompor - limpa o drop\n"
        ret = "/levelup personagem - sobe o nivel do personagem\n"
        ret = "/doar personagem - doa atributos\n"
        ret = "/deletarpersonagem nome - deleta  personagem\n"
        ret = "/deixarmestre - para de ser mestre\n"
         ret = "/querosermestre - assume o papel de mestre\n"
        return ret