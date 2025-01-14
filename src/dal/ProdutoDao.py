from bson import ObjectId

from src.dal.DbConnect import db

produto_collection = db.usuario


class ProdutoDao:
    @staticmethod
    def salva_produto(produto_data):
        try:
            # Inserir o documento no MongoDB
            result = produto_collection.insert_one(produto_data)

            # Criar um dicionário para representar o usuário inserido
            usuario = produto_data.copy()  # Cria uma cópia do dicionário original
            usuario['_id'] = str(result.inserted_id)  # Converte o ObjectId para string

            return usuario
        except Exception as e:
            raise Exception(f"Ocorreu um erro ao criar o usuário: {str(e)}")

    @staticmethod
    def busca_por_descricao(descricao):
        produto = produto_collection.find_one({"descricao": descricao})
        if not produto:
            return None

        produto["_id"] = str(produto["_id"])
        return produto

    @classmethod
    def busca_por_telefone(cls, telefone):
        pass

    @classmethod
    def atualiza_produto(cls, produto_data):
        pass

    @classmethod
    def busca_por_id(cls, id):
        pass

