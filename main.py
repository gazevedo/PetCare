from flask import Flask, request
from dotenv import load_dotenv
from flasgger import Swagger
from flask_cors import CORS

from src.rotas.LojaRota import LojaRota
from src.rotas.UsuarioRota import UsuarioRotas
# from src.rotas.CaixaRota import CaixaRota
import sys

print(sys.executable)
load_dotenv()

# Criar a instância do Flask
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, methods=["GET", "POST", "OPTIONS"])


# Função de validação do token
def verificar_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return {"message": "Token de autenticação não fornecido!"}, 403

    token = auth_header.split(" ")[1]  # Pega o token do formato "Bearer <token>"

    # Aqui você faria a validação do token (com JWT ou outra tecnologia)
    if token != "seu_token_exemplo":
        return {"message": "Token inválido!"}, 403

    return None  # Token válido


# === Configuração do Swagger com Bearer Token ===
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "PetCare API",
        "description": "Documentação da API com autenticação via Bearer Token",
        "version": "1.0"
    },
    "securityDefinitions": {
        "Bearer": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Insira o token no formato: **Bearer &lt;seu_token&gt;**"
        }
    },
    "security": [
        {
            "Bearer": []
        }
    ]
}

swagger = Swagger(app, template=swagger_template)

UsuarioRotas(app)
LojaRota(app)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
