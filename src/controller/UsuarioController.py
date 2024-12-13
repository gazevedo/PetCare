import os
import re

from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError


class UsuarioController:
    @staticmethod
    def validar_email(email):
        """
        Função para validar se o email está no formato correto.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    @classmethod
    def criar_usuario(cls, usuario_data, db):
        usuario_collection = db.usuario

        login = usuario_data.get('login')
        senha = usuario_data.get('senha')

        #valida campos
        if not login or not senha:
            raise BadRequest("Os campos 'login' e 'senha' são obrigatórios.")

        # Validar o e-mail usando o UserController
        if not UsuarioController.validar_email(login):
            raise BadRequest("O campo 'login' deve ser um email válido.")

        #valida duplicado
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
