#!/usr/bin/python
# -*- coding: utf-8 -*-
from models import Mestre

class MestreControle:
    def addMestre(self,dado):
        try:
            mestre = dado[0]
        except:
            return "erro?"

        try:
            Mestre.create(
                usuario=mestre
            )
        except:
            return "Erro adicionar mestre"
        return "%s é um novo mestre" % mestre

    def killMestre(self,dado):
        try:
            mestre = dado[0]
        except:
            return "erro?"

        try:
            (Mestre
             .delete()
             .where(Mestre.usuario == mestre))
        except:
            return "Erro deixar de ser mestre"
        return "%s deixou de ser mestre" % mestre

    @staticmethod
    def mestre(dado):
        try:
            mestre = dado
        except:
            return "erro?"
        try:
            mestre = (Mestre
                .get(Mestre.usuario == mestre))
        except:
            return False
        return True