from bson import ObjectId

from src.dal.DbConnect import db

usuario_collection = db.usuario
tipo_collection = db.usuario_tipo


class UsuarioDao:
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
    def busca_por_email(email, loja):
        usuario = usuario_collection.find_one({"email": email, "loja": loja})
        if not usuario:
            return None
        print("Documento encontrado no MongoDB:", usuario)

        usuario["_id"] = str(usuario["_id"])

        return usuario

    @staticmethod
    def login(usuario_data):
        email = usuario_data.get('email')
        senha = usuario_data.get('senha')
        lojaId = usuario_data.get('loja')

        usuario = usuario_collection.find_one({"email": email, "senha":senha, "lojaId":lojaId})
        if not usuario:
            return None
        print("Documento encontrado no MongoDB:", usuario)

        usuario["_id"] = str(usuario["_id"])
        return usuario

    @staticmethod
    def criar(usuario_data):
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
    def atualizar(id, json):
        result = usuario_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": json}
        )
        return result.modified_count >= 0

    @staticmethod
    def get_tipos():
        """
        Busca todos os tipos de usuário cadastrados na coleção `usuario_tipo`.

        :return: Lista de dicionários com `id`, `descricao` (texto) e `tipo` (número).
        """
        tipos = tipo_collection.find({}, {"_id": 1, "descricao": 1, "tipo": 1})
        return [{"id": str(tipo["_id"]), "descricao": tipo["descricao"], "tipo": tipo.get("tipo", 0)} for tipo in tipos]
