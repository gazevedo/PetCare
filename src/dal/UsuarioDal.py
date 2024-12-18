from bson import ObjectId
from flask import jsonify

from src.dal.DbConnect import db
from src.model.Loja import Loja

usuario_collection = db.usuario


class UsuarioDal:
    @staticmethod
    def busca_por_id(id):
        usuario = usuario_collection.find_one({"_id": ObjectId(id)})
        usuario["_id"] = str(usuario["_id"])
        return usuario

    @staticmethod
    def busca_por_telefone(telefone):
        print("busca_por_telefone dal")
        usuario = usuario_collection.find_one({"telefone": telefone})
        if not usuario:
            return None
        print("Documento encontrado no MongoDB:", usuario)

        usuario["_id"] = str(usuario["_id"])
        return usuario

    @staticmethod
    def salva_usuario(usuario_data):
        try:
            # Inserir o documento no MongoDB
            result = usuario_collection.insert_one(usuario_data)

            # Criar um dicionário para representar o usuário inserido
            usuario = usuario_data.copy()  # Cria uma cópia do dicionário original
            usuario['_id'] = str(result.inserted_id)  # Converte o ObjectId para string

            return usuario
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao criar o usuário: {str(e)}")

    @staticmethod
    def atualiza_usuario(usuario_data):
        try:
            telefone = usuario_data.get('telefone')
            usuario_data.pop('_id', None)

            resultado = usuario_collection.update_one(
                {"telefone": telefone},  # Filtro para encontrar o usuário pelo telefone
                {"$set": usuario_data}  # Dados a serem atualizados
            )

            return usuario_data

        except Exception as e:
            raise Exception(f"Ocorreu um erro ao criar o usuário: {str(e)}")
