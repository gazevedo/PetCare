from urllib import request
from src.controller.ProdutoController import ProdutoController


def ProdutoRota(app):
    """
    Função que registra as rotas de produtos no app Flask
    """

    @app.route("/Produtos/criar_produto", methods=["POST"])
    def criar_produto():
        return ProdutoController.criar_produto(request.get_json())

    @app.route('/Produto/<produto_id>', methods=['PUT'])
    def atualizar_produto(produto_id):
        return ProdutoController.atualizar_produto(produto_id, request.get_json())

    @staticmethod
    @app.route('/Produto/buscar_por_id/<id>', methods=['GET'])
    def buscar_por_id(id):
        return ProdutoController.buscar_por_id(id)

    @staticmethod
    @app.route('/Produto/buscar_por_descricao/<descricao>', methods=['GET'])
    def buscar_por_descricao(descricao):
        return ProdutoController.buscar_por_descricao(descricao)
