import os
import re

from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from flasgger import Swagger
from werkzeug.exceptions import InternalServerError, BadRequest

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

@app.route('/Usuario', methods=['POST'])
def criar_usuario():
    """
    Criar um novo usuário
    ---
    parameters:
      - name: usuario
        in: body
        required: true
        schema:
          type: object
          properties:
            login:
              type: string
            senha:
              type: string
            nome:
              type: string

    responses:
      200:
        description: Usuário criado com sucesso
        schema:
          id: Usuario
    """
    usuario_collection = db.usuario

    usuario_data = request.get_json()
    login = usuario_data.get('login')
    senha = usuario_data.get('senha')

    if not login or not senha:
        raise BadRequest("Os campos 'login' e 'senha' são obrigatórios.")

    if not validar_email(login):
        raise BadRequest("O campo 'login' deve ser um email válido.")

    if usuario_collection.find_one({"login": login}):
        raise BadRequest("Já existe um usuário com este login.")

    usuario = {
        "login": login,
        "senha": senha,
        "nome": usuario_data.get('nome'),
        "telefone": usuario_data.get('telefone'),
        "rua": usuario_data.get('rua'),
        "numero": usuario_data.get('numero'),
        "bairro": usuario_data.get('bairro'),
        "cidade": usuario_data.get('cidade'),
        "loja": os.getenv("loja_id"),
        "tipo": 'client',
        "ativo": 1
    }

    try:
        result = usuario_collection.insert_one(usuario)
        usuario['_id'] = str(result.inserted_id)
        return jsonify(usuario), 201
    except Exception as e:
        raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")


def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(regex, email))

if __name__ == "__main__":
    app.run(debug=True)
