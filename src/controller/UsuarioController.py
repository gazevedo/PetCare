import re

from bson import ObjectId
from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

from src.dal.LojaDao import LojaDao
from src.dal.UsuarioDao import UsuarioDao


class UsuarioController:
    @staticmethod
    def criar_usuario(usuario_data):
        telefone = usuario_data.get('telefone')
        tipo = usuario_data.get('tipo')
        lojaId = usuario_data.get('loja')

        #valida campos
        if not telefone:
            raise BadRequest("Os campos 'telefone' é obrigatório.")

        if not tipo:
            raise BadRequest("O campo 'tipo' é obrigatório.")

        # Valida se o tipo existe
        tipos_existentes = UsuarioDao.get_tipos()
        tipos_validos = [tipo["tipo"] for tipo in tipos_existentes]  # Validar pelo campo 'tipo'
        if tipo not in tipos_validos:
            raise BadRequest(f"O tipo informado não existe.")

        #valida duplicado
        if UsuarioDao.busca_por_telefone(telefone):
            raise BadRequest("Já existe um usuário com este telefone.")

        #valida cliente
        loja = LojaDao.busca_por_id(lojaId)

        if not loja:
            raise BadRequest("Loja não encontrada.")

        try:
            usuario = UsuarioDao.criar(usuario_data)

            return jsonify(usuario), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")

    @staticmethod
    def atualizar_usuario(id, json):
        try:
            telefone = json.get('telefone')
            tipo = json.get('tipo')

            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # valida campos
            if not telefone:
                raise BadRequest("Os campos 'telefone' é obrigatório.")

            if not tipo:
                raise BadRequest("O campo 'tipo' é obrigatório.")

            # Valida se o tipo existe
            tipos_existentes = UsuarioDao.get_tipos()
            tipos_validos = [tipo["tipo"] for tipo in tipos_existentes]  # Validar pelo campo 'tipo'
            if tipo not in tipos_validos:
                raise BadRequest(f"O tipo '{tipo}' não existe.")

            usuario = UsuarioDao.busca_por_id(id)
            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 404
            print("id " + id)
            print("json " + str(json))
            atualizado = UsuarioDao.atualizar(ObjectId(id), json)
            print("result "+str(atualizado))
            if not atualizado:
                return jsonify({"error": "Usuário não encontrado para atualizar"}), 404

            return jsonify({"message": "Usuário atualizado com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500

    @staticmethod
    def busca_por_id(id):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            usuario = UsuarioDao.busca_por_id(id)

            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 500

            return jsonify(usuario), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500

    @staticmethod
    def busca_por_telefone(telefone):
        try:
            usuario = UsuarioDao.busca_por_telefone(telefone)
            if not usuario:
                return jsonify({"error": "Usuário não encontrado"}), 500

            return jsonify(usuario), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500


    @staticmethod
    def validar_email(email):
        """
        Função para validar se o email está no formato correto.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    @staticmethod
    def get_tipos():
        """
        Busca todos os tipos de usuários e os retorna como JSON.

        :return: JSON contendo a lista de tipos de usuários.
        """
        try:
            tipos = UsuarioDao.get_tipos()
            return jsonify(tipos), 200
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao buscar os tipos de usuários: {str(e)}")