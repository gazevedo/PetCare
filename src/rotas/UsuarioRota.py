from flask import request, jsonify
from werkzeug.exceptions import InternalServerError, BadRequest

import os

from src.controller.UsuarioController import UsuarioController


def UsuarioRotas(app, db):
    """
    Função que registra as rotas de usuário no app Flask
    """
    @app.route('/usuario', methods=['POST'])
    def criar_usuario():
        """
        Criar um novo usuário
        ---
        parameters:
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

        responses:
          200:
            description: Usuário criado com sucesso
            schema:
              id: Usuario
        """

        return UsuarioController.criar_usuario(request.get_json(), db);


    # Rota para atualizar o usuário
    @app.route('/usuario/<user_id>', methods=['PUT'])
    def atualizar_usuario(user_id):
        """
        Atualizar informações de um usuário existente
        ---
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
        usuario_collection = db.usuario

        # Obter dados do corpo da requisição
        usuario_data = request.get_json()

        # Buscar o usuário pelo ID
        usuario = usuario_collection.find_one({"_id": user_id})

        if not usuario:
            raise BadRequest("Usuário não encontrado.")

        # Atualizar os dados do usuário
        if 'login' in usuario_data and usuario_data['login']:
            if not UsuarioController.validar_email(usuario_data['login']):
                raise BadRequest("O campo 'login' deve ser um email válido.")
            usuario['login'] = usuario_data['login']

        if 'senha' in usuario_data and usuario_data['senha']:
            usuario['senha'] = usuario_data['senha']

        if 'nome' in usuario_data and usuario_data['nome']:
            usuario['nome'] = usuario_data['nome']

        if 'telefone' in usuario_data and usuario_data['telefone']:
            usuario['telefone'] = usuario_data['telefone']

        if 'rua' in usuario_data and usuario_data['rua']:
            usuario['rua'] = usuario_data['rua']

        if 'numero' in usuario_data and usuario_data['numero']:
            usuario['numero'] = usuario_data['numero']

        if 'bairro' in usuario_data and usuario_data['bairro']:
            usuario['bairro'] = usuario_data['bairro']

        if 'cidade' in usuario_data and usuario_data['cidade']:
            usuario['cidade'] = usuario_data['cidade']

        try:
            # Atualiza o usuário no banco de dados
            usuario_collection.update_one({"_id": user_id}, {"$set": usuario})
            return jsonify(usuario), 200
        except Exception as e:
            raise InternalServerError(f"Ocorreu um erro ao atualizar o usuário: {str(e)}")