from bson import ObjectId
from flask import jsonify

from src.dal.LojaDao import LojaDao


class LojaController:
    @staticmethod
    def busca_por_id(id):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            loja = LojaDao.busca_por_id(id)

            if not loja:
                return jsonify({"error": "Loja não encontrada"}), 500

            return jsonify(loja), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar a loja: {str(e)}"}), 500

    @staticmethod
    def busca_por_telefone(telefone):
        try:
            loja = LojaDao.busca_por_telefone(telefone)

            if not loja:
                return jsonify({"error": "Loja não encontrada"}), 404

            return jsonify(loja), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar a loja: {str(e)}"}), 500

    @staticmethod
    def atualizar(id, json):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Validar se os campos atualizados seguem o esquema correto
            allowed_fields = ["nome", "telefone", "rua", "numero", "bairro", "cidade", "cep", "status"]
            invalid_fields = [field for field in json.keys() if field not in allowed_fields]

            if invalid_fields:
                return jsonify({"error": f"Campos inválidos: {', '.join(invalid_fields)}"}), 400

            # Atualizar os dados no banco de dados
            atualizado = LojaDao.atualizar(ObjectId(id), json)

            if not atualizado:
                return jsonify({"error": "Loja não encontrada para atualizar"}), 404

            return jsonify({"message": "Loja atualizada com sucesso"}), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao atualizar a loja: {str(e)}"}), 500

    @staticmethod
    def criar(json):
        try:
            # Validar os dados recebidos
            required_fields = ["nome", "telefone", "rua", "numero", "bairro", "cidade", "cep"]
            missing_fields = [field for field in required_fields if field not in json]

            if missing_fields:
                return jsonify({"error": f"Campos obrigatórios ausentes: {', '.join(missing_fields)}"}), 400

            # Validar se a loja já existe no banco
            loja_existente = LojaDao.busca_por_telefone(json.get("telefone"))
            if loja_existente:
                return jsonify({"error": "Uma loja com este telefone já existe"}), 409

            json["status"] = 1

            # Inserir no banco de dados
            loja_id = LojaDao.criar(json)

            return jsonify({"message": "Loja criada com sucesso", "id": str(loja_id)}), 201
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao criar a loja: {str(e)}"}), 500


