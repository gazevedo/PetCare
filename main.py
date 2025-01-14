# main.py
import os
from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv
from flasgger import Swagger

from src.rotas.LojaRota import LojaRota
from src.rotas.UsuarioRota import UsuarioRotas
from src.rotas.CaixaRota import CaixaRota

load_dotenv()

# Criar a instância do Flask
app = Flask(__name__)

# Integrar o Swagger com o Flask
swagger = Swagger(app)

# Registrar as rotas
UsuarioRotas(app)
LojaRota(app)
CaixaRota(app)

if __name__ == "__main__":
    app.run(debug=True)
