from flask import request, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest
from src.controller.UsuarioController import UsuarioController
from src.model.Usuario import Usuario


def UsuarioRotas(app):
    """
    Função que registra as rotas de usuário no app Flask
    """

    @app.route('/Usuario', methods=['POST'])
    def criar_usuario():
        """
        Criar um novo usuário
        ---
        tags:
          - Usuario
        parameters:
          - name: telefone
            in: body
            required: true
            schema:
              type: object
              properties:
                login:
                  type: string
                senha:
                  type: string
                nome:
                  type: string
                cpf:
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
                loja:
                    type: string
                tipo:
                    type: string
                status:
                    type: string

        responses:
          200:
            description: Usuário criado com sucesso
            schema:
              id: Usuario
        """

        return UsuarioController.criar_usuario(request.get_json())

    # Rota para atualizar o usuário
    @app.route('/Usuario/<user_id>', methods=['PUT'])
    def atualizar_usuario(user_id):
        """
        Atualizar informações de um usuário existente
        ---
        tags:
          - Usuario
        parameters:
          - name: user_id
            in: path
            required: true
            type: string
          - name: usuario
            in: body
            required: true
            schema:
              type: object
              properties:
                login:
                  type: string
                senha:
                  type: string
                nome:
                  type: string
                cpf:
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
                loja:
                    type: string
                tipo:
                    type: string
                status:
                    type: string

        responses:
          200:
            description: Usuário atualizado com sucesso
            schema:
              id: Usuario
        """

        return UsuarioController.atualizar_usuario(request.get_json())

    @app.route('/Usuario/<user_id>', methods=['GET'])
    def buscar_por_id(user_id):
        """
        Obter informações de um usuário pelo ID
        ---
        tags:
          - Usuario
        parameters:
          - name: user_id
            in: path
            required: true
            type: string

        responses:
          200:
            description: Informações do usuário retornadas com sucesso
            schema:
              type: object
              properties:
                login:
                  type: string
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
                loja:
                    type: string
                tipo:
                    type: string
                status:
                    type: string
          404:
            description: Usuário não encontrado
        """
        print("busca_por_id " + user_id)
        return UsuarioController.busca_por_id(user_id)

    @app.route('/Usuario/telefone/<telefone>', methods=['GET'])
    def buscar_por_telefone(telefone):
        """
        Obter informações de um usuário pelo telefone
        ---
        tags:
          - Usuario
        parameters:
          - name: telefone
            in: path
            required: true
            type: string

        responses:
          200:
            description: Informações do usuário retornadas com sucesso
            schema:
              type: object
              properties:
                login:
                  type: string
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
                loja:
                    type: string
                tipo:
                    type: string
                status:
                    type: string
          404:
            description: Usuário não encontrado
        """
        print("busca_por_telefone "+telefone)
        return UsuarioController.busca_por_telefone(telefone)
