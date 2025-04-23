import re
import jwt
from bson import ObjectId
from flask import request, jsonify
from werkzeug.exceptions import BadRequest, NotFound, Unauthorized, InternalServerError
from src.dal.UsuarioDao import UsuarioDao
from src.helper.JwtHelper import gerar_token, token_decode_id
from src.model.Usuario import Usuario


class UsuarioController:

    @staticmethod
    def auth_usuario(usuario_data):
        email = usuario_data.get('email')
        senha = usuario_data.get('senha')
        loja = usuario_data.get('loja')

        if not email or not senha or not loja:
            raise BadRequest("Usuário inválido")

        usuario = UsuarioDao.busca_por_email(email, loja)
        if usuario and usuario['email'] == email and usuario['senha'] == senha and usuario['loja'] == loja:
            token = gerar_token(usuario)
            return token
        else:
            raise Unauthorized("Autenticação inválida.")

    @staticmethod
    def criar_usuario(usuario_data):
        email = usuario_data.get('email')
        lojaId = usuario_data.get('loja')
        senha = usuario_data.get('senha')
        tipo = usuario_data.get('tipo')
        telefone = usuario_data.get('telefone')

        if not email:
            raise BadRequest("O campo 'email' é obrigatório.")
        if not telefone:
            raise BadRequest("O campo 'telefone' é obrigatório.")
        if not tipo:
            raise BadRequest("O campo 'tipo' é obrigatório.")
        if not lojaId:
            raise BadRequest("O campo 'lojaId' é obrigatório.")
        if not senha:
            raise BadRequest("O campo 'senha' é obrigatório.")

        tipos_existentes = UsuarioDao.get_tipos()
        tipos_validos = [tipo["tipo"] for tipo in tipos_existentes]
        if tipo not in tipos_validos:
            raise BadRequest("O tipo informado não existe.")

        if UsuarioDao.busca_por_email(email, lojaId):
            raise BadRequest("Já existe um usuário com este email.")

        try:
            usuario = UsuarioDao.criar(usuario_data)
            return usuario
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o usuário: {str(e)}")

    @staticmethod
    def atualizar_usuario(id, json):
        try:
            telefone = json.get('telefone')
            tipo = json.get('tipo')

            if not ObjectId.is_valid(id):
                raise BadRequest("ID inválido.")

            if not telefone:
                raise BadRequest("O campo 'telefone' é obrigatório.")
            if not tipo:
                raise BadRequest("O campo 'tipo' é obrigatório.")

            tipos_existentes = UsuarioDao.get_tipos()
            tipos_validos = [tipo["tipo"] for tipo in tipos_existentes]
            if tipo not in tipos_validos:
                raise BadRequest(f"O tipo '{tipo}' não existe.")

            usuario = UsuarioDao.busca_por_id(id)
            if not usuario:
                raise NotFound("Usuário não encontrado.")

            atualizado = UsuarioDao.atualizar(ObjectId(id), json)
            if not atualizado:
                raise NotFound("Usuário não encontrado para atualizar.")

            return jsonify({"message": "Usuário atualizado com sucesso"}), 200

        except (BadRequest, NotFound) as e:
            raise e
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao atualizar o usuário: {str(e)}")

    @staticmethod
    def busca_usuario():
        try:
            auth_header = request.headers.get('Authorization')
            if not auth_header:
                raise Unauthorized("Token de autorização não fornecido.")

            usuario_id = token_decode_id(auth_header)
            if not usuario_id:
                raise Unauthorized("Token inválido ou expirado.")

            usuario = UsuarioDao.busca_por_id(usuario_id)
            if not usuario:
                raise NotFound("Usuário não encontrado.")

            usuario.pop('senha', None)
            return jsonify(usuario), 200

        except (BadRequest, NotFound, Unauthorized) as e:
            raise e
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao buscar o usuário: {str(e)}")

    @staticmethod
    def busca_por_id(id):
        try:
            if not ObjectId.is_valid(id):
                raise BadRequest("ID inválido.")

            usuario = UsuarioDao.busca_por_id(id)
            if not usuario:
                raise NotFound("Usuário não encontrado.")

            return jsonify(usuario), 200

        except (BadRequest, NotFound) as e:
            raise e
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao buscar o usuário: {str(e)}")

    @staticmethod
    def busca_por_telefone(telefone):
        try:
            usuario = UsuarioDao.busca_por_telefone(telefone)
            if not usuario:
                raise NotFound("Usuário não encontrado.")

            return jsonify(usuario), 200

        except NotFound as e:
            raise e
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao buscar o usuário: {str(e)}")

    @staticmethod
    def validar_email(email):
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    @staticmethod
    def get_tipos():
        try:
            tipos = UsuarioDao.get_tipos()
            return jsonify(tipos), 200
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao buscar os tipos de usuários: {str(e)}")
