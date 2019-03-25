

import random
import urllib.request
import json


class ZoeiraService():
    def apresentar(self):
        return "Oi, Sou prodestinho seu amiguinho!"

    def chaves(self):
        URL = "https://rpgmesa.herokuapp.com/rest/chaves/"
        try:
            url = urllib.request.urlopen(URL)
            chaves = json.loads(url.read().decode())
        except:
            return'Erro na api, tente mais tarde'
        return chaves

    def respostas(self, chave):
        URL = "https://rpgmesa.herokuapp.com/rest/chave/"
        try:
            url = urllib.request.urlopen(URL+'/'+chave)
            respostas = json.loads(url.read().decode())
        except:
            return'Erro na api, tente mais tarde'
        return respostas
