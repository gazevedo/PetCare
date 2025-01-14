from bson import ObjectId

from src.dal.DbConnect import db

loja_collection = db.loja


class LojaDao:
    @staticmethod
    def busca_por_id(id):
        loja = loja_collection.find_one({"_id": ObjectId(id)})
        loja["_id"] = str(loja["_id"])
        return loja

    @staticmethod
    def busca_por_telefone(telefone):
        loja = loja_collection.find_one({"telefone": telefone})
        if loja:  # Garantir que o retorno seja formatado apenas se encontrar uma loja
            loja["_id"] = str(loja["_id"])
        return loja

    @staticmethod
    def atualizar(id, json):
        """
        Atualiza uma loja existente no banco de dados.
        :param id: ID da loja a ser atualizada.
        :param json: Dados a serem atualizados.
        :return: True se a atualização foi bem-sucedida, False caso contrário.
        """
        result = loja_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": json}
        )
        return result.modified_count >= 0

    @staticmethod
    def criar(json):
        """
        Cria uma nova loja no banco de dados.
        :param json: Dados da loja a ser criada.
        :return: ID da loja criada.
        """
        result = loja_collection.insert_one(json)
        return str(result.inserted_id)
