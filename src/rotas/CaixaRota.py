from flask import request, jsonify
from src.controller.CaixaController import CaixaController


def CaixaRota(app):
    """
    Define as rotas relacionadas ao Caixa.
    """
    @app.route('/Caixa/buscar_por_id/<id>', methods=['GET'])
    def buscar_caixa_por_id(id):
        """
        Obter informações de um caixa pelo ID.
        ---
        tags:
          - Caixa
        parameters:
          - name: id
            in: path
            required: true
            type: string
        responses:
          200:
            description: Informações do caixa retornadas com sucesso.
          404:
            description: Caixa não encontrado.
        """
        return CaixaController.buscar_por_id(id)

    @app.route('/Caixa/buscar_tipos_movimentacao', methods=['GET'])
    def buscar_tipos_movimentacao():
        """
        Buscar todos os tipos de movimentação.
        ---
        tags:
          - Caixa
        responses:
          200:
            description: Lista de tipos de movimentação disponíveis.
            content:
              application/json:
                schema:
                  type: array
                  items:
                    type: object
                    properties:
                      id:
                        type: string
                        description: Identificador do tipo de movimentação.
                      descricao:
                        type: string
                        description: Descrição do tipo de movimentação.

        """
        return CaixaController.buscar_tipos_movimentacao()

    @app.route('/Caixa/registrar_movimentacao', methods=['POST'])
    def registrar_movimentacao():
        """
        registrar uma nova movimentação financeira.
        ---
        tags:
          - Caixa
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                caixaId:
                  type: string
                tipoId:
                  type: string
                valor:
                  type: number
                  format: float
                data:
                  type: string
                  format: date-time
        responses:
          201:
            description: Movimentação criada com sucesso.
          400:
            description: Erro na validação dos dados enviados.
        """
        return CaixaController.registrar_movimentacao(request.json)

    @app.route('/Caixa/buscar_movimentacoes', methods=['GET'])
    def buscar_movimentacoes():
        """
        Buscar movimentações por período e filtros.
        ---
        tags:
          - Caixa
        parameters:
          - name: caixaId
            in: query
            required: false
            type: string
          - name: usuarioId
            in: query
            required: false
            type: string
          - name: inicio
            in: query
            required: false
            type: string
            format: date-time
          - name: fim
            in: query
            required: false
            type: string
            format: date-time
        responses:
          200:
            description: Lista de movimentações.
            schema:
              type: array
              items:
                type: object
                properties:
                  id:
                    type: string
                  valor:
                    type: number
                  tipo:
                    type: string
                  data:
                    type: string
                    format: date-time
        """

        return CaixaController.buscar_movimentacoes(request.json)
