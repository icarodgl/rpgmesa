import json
import urllib.request
import urllib.parse


class ZoeiraService:
    def chaves(self):
        URL = "https://rpgmesa.herokuapp.com/rest/chaves/"
        try:
            url = urllib.request.urlopen(URL)
            chaves = json.loads(url.read().decode())
        except:
            return {'respostas':['comé que é?']}
        return chaves

    def respostas(self, chave):
        URL = 'https://rpgmesa.herokuapp.com/rest/chave/%d'%chave['id']
        try:
            url = urllib.request.urlopen(URL)
            respostas = json.loads(url.read().decode())
        except:
            return{'respostas':['escreve direiro seu minecraft!']}
        return respostas
