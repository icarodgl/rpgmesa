from flask import Flask, request
from flask_restful import Resource, Api
import os
from json import dumps

app = Flask(__name__)
api = Api(app)


class Servidor(Resource):
    def get(self):
        m = {"mensagem": "estou vivo!"}
        return m


'''
@app.route("/")
def hello():
    m = {"Mensagem":"Ligado"}
    return m
'''

api.add_resource(Servidor, '/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
