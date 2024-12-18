from bson import ObjectId
from flask import request, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest
from src.controller.LojaController import LojaController


def LojaRota(app):
    """
    """
    @app.route('/Loja/<id>', methods=['GET'])
    def busca_por_id(id):
        """
        Obter informações de uma loja pelo ID
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
            description: Informações da loja retornadas com sucesso
            schema:
              type: object
              properties:
                nome:
                  type: string
                bairro:
                  type: string
                cidade:
                  type: string
                numero:
                  type: string
                rua:
                  type: string
                status:
                  type: string
                telefone:
                  type: string
          404:
            description: Loja não encontrada
        """
        return LojaController.busca_por_id(id)

    @app.route('/Loja/telefone/<telefone>', methods=['GET'])
    def busca_por_telefone(telefone):
        """
        Obter informações de uma loja pelo ID
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
            description: Informações da loja retornadas com sucesso
            schema:
              type: object
              properties:
                nome:
                  type: string
                bairro:
                  type: string
                cidade:
                  type: string
                numero:
                  type: string
                rua:
                  type: string
                status:
                  type: string
                telefone:
                  type: string
          404:
            description: Loja não encontrada
        """
        return LojaController.busca_por_telefone(telefone)

