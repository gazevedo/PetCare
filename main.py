import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
from flasgger import Swagger
from werkzeug.exceptions import BadRequest

# Carregar variáveis do arquivo .env
from controller.UsuarioController import UsuarioController

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

# Instância do controlador de usuário
usuario_controller = UsuarioController(db)


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
    usuario_data = request.get_json()
    return usuario_controller.criar_usuario(usuario_data)


if __name__ == "__main__":
    app.run(debug=True)
