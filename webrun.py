from flask import Flask, request,jsonify
from flask_restful import Resource, Api
import os   
import json
from models import *

app = Flask(__name__)
api = Api(app)


class Servidor(Resource):
    def get(self):
        m = {"mensagem": "estou vivo!"}
        return m

class Personagen (Resource):
    def get(self, nome):
        personagem = Personagem.get(Personagem.nome == nome)
        res =  {
            "nome": personagem.nome,
            "level": personagem.nivel,
            "vida": personagem.vida,
            "vida maxima": personagem.vidamax,
            "pontos":personagem.pontos,
            "atributos":[
                {"força":personagem.forca},
                {"destreza":personagem.destreza},
                {"inteligencia":personagem.inteligencia},
                {"agilidade":personagem.agilidade},
                {"resiliencia":personagem.resiliencia}
            ],
            }
        return jsonify(res)
class Personagens (Resource):
    def get(self):
        res = []
        query = Personagem.select()
        for personagem in query:
            res.append({
            "nome": personagem.nome,
            "level": personagem.nivel,
            "vida": personagem.vida,
            "vida maxima": personagem.vidamax,
            "pontos":personagem.pontos,
            "atributos":[
                {"força":personagem.forca},
                {"destreza":personagem.destreza},
                {"inteligencia":personagem.inteligencia},
                {"agilidade":personagem.agilidade},
                {"resiliencia":personagem.resiliencia}
            ],
            })
        return res

api.add_resource(Servidor, '/')
api.add_resource(Personagens, '/personagens/')
api.add_resource(Personagen, '/personagem/<nome>')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
