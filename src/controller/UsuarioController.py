import re

from bson import ObjectId
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

    @staticmethod
    def criar_usuario(usuario_data):
        telefone = usuario_data.get('telefone')

        #valida campos
        if not telefone:
            raise BadRequest("Os campos 'telefone' é obrigatório.")

        #valida duplicado
        if UsuarioDal.busca_por_telefone(telefone):
            raise BadRequest("Já existe um usuário com este telefone.")

        try:
            usuario = UsuarioDal.salva_usuario(usuario_data)

            return jsonify(usuario), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")

    @staticmethod
    def atualizar_usuario(usuario_data):
        try:
            telefone = usuario_data.get('telefone')
            usuario = UsuarioDal.busca_por_telefone(telefone)
            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 500

            usuario =  UsuarioDal.atualiza_usuario(usuario_data)
            return jsonify(usuario), 201
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500

    @staticmethod
    def busca_por_id(id):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            usuario = UsuarioDal.busca_por_id(id)

            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 500

            return jsonify(usuario), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500

    @staticmethod
    def busca_por_telefone(telefone):
        print("busca_por_telefone ctr")
        try:
            usuario = UsuarioDal.busca_por_telefone(telefone)
            print("retornou busca")
            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 500

            return jsonify(usuario), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500
