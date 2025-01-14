from flask import request, jsonify
from src.controller.LojaController import LojaController


def LojaRota(app):
    """
    Define as rotas relacionadas à Loja.
    """

    @app.route('/Loja/criar_loja', methods=['POST'])
    def criar_loja():
        """
        Criar uma nova loja.
        ---
        tags:
          - Loja
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                telefone:
                  type: string
                rua:
                  type: string
                numero:
                  type: string
                bairro:
                  type: string
                cidade:
                  type: string
                cep:
                  type: string
        responses:
          201:
            description: Loja criada com sucesso.
          400:
            description: Erro na validação dos dados enviados.
        """
        return LojaController.criar(request.json)

    @app.route('/Loja/atualizar_loja/<id>', methods=['PUT'])
    def atualizar_loja(id):
        """
        Atualizar uma loja existente pelo ID.
        ---
        tags:
          - Loja
        parameters:
          - name: id
            in: path
            required: true
            type: string
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                nome:
                  type: string
                telefone:
                  type: string
                rua:
                  type: string
                numero:
                  type: string
                bairro:
                  type: string
                cidade:
                  type: string
                cep:
                  type: string
                status:
                  type: string
        responses:
          200:
            description: Loja atualizada com sucesso.
          400:
            description: Erro na validação dos dados enviados.
          404:
            description: Loja não encontrada.
        """
        return LojaController.atualizar(id, request.json)

    @app.route('/Loja/busca_por_id/<id>', methods=['GET'])
    def busca_por_id(id):
        """
        Obter informações de uma loja pelo ID.
        ---
        tags:
          - Loja
        parameters:
          - name: id
            in: path
            required: true
            type: string
        responses:
          200:
            description: Informações da loja retornadas com sucesso.
          404:
            description: Loja não encontrada.
        """
        return LojaController.busca_por_id(id)

    @app.route('/Loja/busca_por_telefone/<telefone>', methods=['GET'])
    def busca_por_telefone(telefone):
        """
        Obter informações de uma loja pelo telefone.
        ---
        tags:
          - Loja
        parameters:
          - name: telefone
            in: path
            required: true
            type: string
        responses:
          200:
            description: Informações da loja retornadas com sucesso.
          404:
            description: Loja não encontrada.
        """
        return LojaController.busca_por_telefone(telefone)
