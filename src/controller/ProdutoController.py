from bson import ObjectId
from flask import jsonify
from werkzeug.exceptions import BadRequest, InternalServerError

from src.dal.ProdutoDao import ProdutoDao


class ProdutoController:
    @staticmethod
    def criar_produto(produto_data):
        descricao = produto_data.get('descricao')  # Corrigi 'decricao' para 'descricao'

        # Valida campos
        if not descricao:
            raise BadRequest("O campo 'descricao' é obrigatório.")  # Corrigido para 'descricao'

        # Verifica duplicado
        if ProdutoDao.busca_por_descricao(descricao):
            raise BadRequest("Já existe um produto com esta descrição.")

        try:
            produto = ProdutoDao.salva_produto(produto_data)
            return jsonify(produto), 201
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao criar o produto: {str(e)}")  # Corrigido 'prouto' para 'produto'

    @staticmethod
    def atualizar_produto(produto_data):
        try:
            descricao = produto_data.get('descricao')  # Corrigi 'produto' para 'descricao' para buscar corretamente

            if not descricao:
                return jsonify({"error": "Descrição do produto não encontrada."}), 400  # Mudado para 400 por falta de dados obrigatórios

            produto = ProdutoDao.atualiza_produto(produto_data)
            if produto:
                return jsonify(produto), 200  # Retorno 200 para sucesso na atualização
            else:
                return jsonify({"error": "Produto não encontrado para atualização."}), 404  # 404 caso o produto não exista
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao atualizar o produto: {str(e)}"}), 500

    @staticmethod
    def buscar_por_id(id):
        try:
            # Verificar se o id é um ObjectId válido
            if not ObjectId.is_valid(id):
                return jsonify({"error": "ID inválido"}), 400

            # Converter id para ObjectId
            produto = ProdutoDao.busca_por_id(id)

            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 404  # Alterado para 404 quando não encontrado

            return jsonify(produto), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o produto: {str(e)}"}), 500

    @staticmethod
    def buscar_por_descricao(descricao):
        try:
            produto = ProdutoDao.busca_por_descricao(descricao)
            if not produto:
                return jsonify({"error": "Produto não encontrado"}), 404  # Alterado para 404 quando não encontrado

            return jsonify(produto), 200
        except Exception as e:
            return jsonify({"error": f"Ocorreu um erro ao buscar o produto: {str(e)}"}), 500
