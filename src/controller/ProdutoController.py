from bson import ObjectId
from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

from src.dal.ProdutoDao import ProdutoDao


class ProdutoController:
    @staticmethod
    def criar_produto(produto_data):
        descricao = produto_data.get('decricao')

        # valida campos
        if not descricao:
            raise BadRequest("Os campos 'descricao' é obrigatório.")

        # valida duplicado
        if ProdutoDao.busca_por_descricao(descricao):
            raise BadRequest("Já existe um usuário com este telefone.")

        try:
            produto = ProdutoDao.salva_produto(produto_data)
            return jsonify(produto), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o prouto: {str(e)}")

    @staticmethod
    def atualizar_produto(produto_data):
        try:
            produto = produto_data.get('descricao')

            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 500

            produto = ProdutoDao.atualiza_produto(produto_data)
            return jsonify(produto), 201
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o usuário: {str(e)}"}), 500

    @staticmethod
    def buscar_por_id(id):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            produto = ProdutoDao.busca_por_id(id)

            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 500

            return jsonify(produto), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o produto: {str(e)}"}), 500

    @staticmethod
    def buscar_por_descricao(descricao):
        try:
            produto = ProdutoDao.busca_por_descricao(descricao)
            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 500

            return jsonify(produto), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o produto: {str(e)}"}), 500






