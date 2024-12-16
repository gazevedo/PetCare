import re

from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

from src.dal.UsuarioDal import UsuarioDal


class UsuarioController:
    @staticmethod
    def validar_email(email):
        """
        Função para validar se o email está no formato correto.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    @classmethod
    def criarUsuario(cls, usuario_data):
        telefone = usuario_data.get('telefone')

        # #valida campos
        if not telefone:
            raise BadRequest("Os campos 'telefone' é obrigatório.")

        #valida duplicado
        if UsuarioDal.getUsuarioTelefone(telefone):
            raise BadRequest("Já existe um usuário com este telefone.")

        try:
            usuario = UsuarioDal.SalvarUsuario(usuario_data)

            return jsonify(usuario), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")
