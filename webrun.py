from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
app = Flask(__name__)
api = Api(app)

class Servidor(Resource):
    def get(self):
        m ={"mensagem":"estou vivo!"}
        return m

'''
@app.route("/")
def hello():
    m = {"Mensagem":"Ligado"}
    return m'''

api.add_resource(Servidor, '/')
if __name__ == '__main__':
    app.run(port='8000')
