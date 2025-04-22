from bson import ObjectId
from flask import jsonify

from src.dal.DbConnect import db

caixa_collection = db.caixa
movimentacao_tipo_collection = db.movimentacao_tipo
movimentacao_collection = db.movimentacao


class CaixaDao:
    @staticmethod
    def busca_por_id(id):
        """
        Busca um caixa pelo ID.
        :param id: ID do caixa.
        :return: Dados do caixa ou None se não encontrado.
        """
        try:
            caixa = caixa_collection.find_one({"_id": ObjectId(id)})
            if caixa:
                caixa["_id"] = str(caixa["_id"])  # Converter ObjectId para string
            return caixa
        except Exception as e:
            print(f"Erro ao buscar caixa por ID: {e}")
            return None

    @staticmethod
    def criar(json):
        """
        Cria um novo caixa no banco de dados.
        :param json: Dados do caixa a ser criado.
        :return: ID do caixa criado.
        """
        try:
            result = caixa_collection.insert_one(json)
            return str(result.inserted_id)
        except Exception as e:
            print(f"Erro ao criar caixa: {e}")
            return None

    @staticmethod
    def atualizar(id, json):
        """
        Atualiza um caixa existente no banco de dados.
        :param id: ID do caixa a ser atualizado.
        :param json: Dados a serem atualizados.
        :return: True se atualizado com sucesso, False caso contrário.
        """
        try:
            result = caixa_collection.update_one(
                {"_id": ObjectId(id)}, {"$set": json}
            )
            return result.modified_count > 0
        except Exception as e:
            print(f"Erro ao atualizar caixa: {e}")
            return False

    @staticmethod
    def buscar_por_id(id):
        """
        Alias para o método estático busca_por_id.
        """
        caixa = caixa_collection.find_one({"_id": ObjectId(id)})
        caixa["_id"] = str(caixa["_id"])
        return caixa

    @classmethod
    def buscar_movimentacoes(cls, filtro):
        pass

    @staticmethod
    def buscar_tipos_movimentacao():
        """
        Busca os tipos de movimentação no banco de dados.
        """
        tipos = movimentacao_tipo_collection.find({})
        return [{"id": str(tipo["_id"]), "tipo": tipo["tipo"], "descricao": tipo["descricao"]} for tipo in tipos]

    @staticmethod
    def salvar_movimentacao(movimentacao):
        result = movimentacao_collection.insert_one(movimentacao)
        return str(result.inserted_id)

    @staticmethod
    def buscar_caixa_aberto(loja_id, usuario_id):
        try:
            # Consultando o banco com PyMongo
            caixa_aberto = movimentacao_collection.find_one({
                "lojaID": loja_id,
                "usuarioId": usuario_id,
                "dataFechamento": None
            })
            return caixa_aberto
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao buscar caixa aberto: {str(e)}")


