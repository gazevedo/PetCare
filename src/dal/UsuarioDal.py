from bson import ObjectId
from flask import jsonify

from src.dal.DbConnect import db
from src.model.Loja import Loja

usuario_collection = db.usuario

class UsuarioDal:
    @staticmethod
    def getUsuarioId(id):
        usuario = usuario_collection.find_one({"_id": ObjectId(id)})
        usuario["_id"] = str(usuario["_id"])
        return usuario

    @staticmethod
    def getUsuarioTelefone(telefone):
        usuario = usuario_collection.find_one({"telefone": telefone})
        if not usuario:
            return None
        usuario["_id"] = str(usuario["_id"])
        return usuario

    @classmethod
    def SalvarUsuario(cls, usuario_data):
        try:
            # Inserir o documento no MongoDB
            result = usuario_collection.insert_one(usuario_data)

            # Criar um dicionário para representar o usuário inserido
            usuario = usuario_data.copy()  # Cria uma cópia do dicionário original
            usuario['_id'] = str(result.inserted_id)  # Converte o ObjectId para string

            return usuario
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao criar o usuário: {str(e)}")
