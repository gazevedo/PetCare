from werkzeug.exceptions import BadRequest, InternalServerError
from flask import jsonify
import re
import os

class UsuarioController:
    def __init__(self, db):
        self.db = db
        self.usuario_collection = db.usuario

    @staticmethod
    def validar_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    def criar_usuario(self, usuario_data):
        login = usuario_data.get('login')
        senha = usuario_data.get('senha')

        if not login or not senha:
            raise BadRequest("Os campos 'login' e 'senha' são obrigatórios.")

        if not self.validar_email(login):
            raise BadRequest("O campo 'login' deve ser um email válido.")

        if self.usuario_collection.find_one({"login": login}):
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
            result = self.usuario_collection.insert_one(usuario)
            usuario['_id'] = str(result.inserted_id)
            return jsonify(usuario), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")
