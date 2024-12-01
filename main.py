# main.py
import os
from flask import Flask
from pymongo import MongoClient
from dotenv import load_dotenv
from flasgger import Swagger
from src.rotas.UsuarioRota import UsuarioRotas

load_dotenv()

# Criar a instância do Flask
app = Flask(__name__)

# Integrar o Swagger com o Flask
swagger = Swagger(app)

# Obter a URI do MongoDB diretamente do .env
MONGO_URI = os.getenv("MONGO_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")  # Nome do banco de dados

# Conectar ao MongoDB
client = MongoClient(MONGO_URI)

# Especificar o banco de dados
db = client[DATABASE_NAME]  # Defina o banco de dados

# Registrar as rotas
UsuarioRotas(app, db)

if __name__ == "__main__":
    app.run(debug=True)
