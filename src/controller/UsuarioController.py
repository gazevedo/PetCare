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

        # login = usuario_data.get('login')
        # senha = usuario_data.get('senha')
        telefone = usuario_data.get('telefone')

        # #valida campos
        if not telefone:
            raise BadRequest("Os campos 'telefone' é obrigatório.")

        #valida duplicado
        if usuario_collection.find_one({"telefone": telefone}):
            raise BadRequest("Já existe um usuário com este login.")

        try:
            result = usuario_collection.insert_one(usuario_data)
            usuario_data['_id'] = str(result.inserted_id)
            return jsonify(usuario_data), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")
