#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import Cenario


class CenarioControle():
    def cria(self, dados):
        try:
            nome = dados[1]
            descricao = ' '.join(map(str, dados[2:]))
        except:
            return "Erro, tente: /criacenario Nome uma descrição do mesmo"
        try:
            cenario = Cenario.create(
                nome=nome,
                descricao=descricao
            )
        except:
            return "erro ao criar cenario"
        return cenario.nome + ": " + cenario.descricao

    def cenario(self, dados):
        try:
            cenario = Cenario.get(Cenario.nome == dados[1])
        except:
            return "Cenario não encontrado"
        return cenario.nome + ": " + cenario.descricao
