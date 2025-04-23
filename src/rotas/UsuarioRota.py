from flask import request, jsonify
from src.controller.UsuarioController import UsuarioController


def UsuarioRotas(app):
    """
    Função que registra as rotas de usuário no app Flask
    """

    @app.route('/Usuario/criar_usuario', methods=['POST'])
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
        responses:
          200:
            description: Usuário criado com sucesso
            schema:
              id: Usuario
        """

        # Verifique se a função retorna um JSON válido
        resultado = UsuarioController.criar_usuario(request.get_json())
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Erro ao criar usuário"}), 400  # Erro de criação

    # Rota para autenticar usuario
    @app.route('/Usuario/auth_usuario', methods=["POST", "OPTIONS"])
    def auth_usuario():
        """
        Autenticar usuário
        ---
        tags:
          - Usuario
        parameters:
          - name: body
            in: body
            required: true
            schema:
              type: object
              properties:
                login:
                  type: string
                senha:
                  type: string
                storeId:
                  type: string
        responses:
          200:
            description: Usuário autenticado com sucesso
            schema:
              id: Usuario
          401:
            description: Credenciais inválidas
        """
        resultado = UsuarioController.auth_usuario(request.get_json())
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Erro ao autenticar usuário"}), 500  # Erro de criação

    # Rota para atualizar o usuário
    @app.route('/Usuario/atualizar_usuario/<id>', methods=['PUT'])
    def atualizar_usuario(id):
        """
        Atualizar informações de um usuário existente
        ---
        tags:
          - Usuario
        parameters:
          - name: id
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

        resultado = UsuarioController.atualizar_usuario(id, request.get_json())
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Erro ao atualizar usuário"}), 400  # Erro de atualização

    @app.route('/Usuario/buscar_por_id/<id>', methods=['GET'])
    def buscar_por_id(id):
        """
        Obter informações de um usuário pelo ID
        ---
        tags:
          - Usuario
        parameters:
          - name: id
            in: path
            required: true
            type: string
        responses:
          200:
            description: Informações do usuário retornadas com sucesso
          404:
            description: Usuário não encontrado
        """
        resultado = UsuarioController.busca_por_id(id)
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404  # Erro caso não encontre o usuário

    @app.route('/Usuario/buscar_usuario', methods=['GET'])
    def buscar_usuario():
        """
        Obter informações do usuário autenticado via token JWT
        ---
        tags:
          - Usuario
        security:
          - BearerAuth: []
        responses:
          200:
            description: Informações do usuário retornadas com sucesso
          401:
            description: Token inválido ou expirado
          404:
            description: Usuário não encontrado
        """
        resultado, status = UsuarioController.busca_usuario()
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404  # Erro caso não encontre o usuário


    @app.route('/Usuario/buscar_por_telefone/<telefone>', methods=['GET'])
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
        resultado = UsuarioController.busca_por_telefone(telefone)
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Usuário não encontrado"}), 404  # Erro caso não encontre o usuário

    @app.route('/Usuario/buscar_tipos', methods=['GET'])
    def get_tipos():
        """
        Endpoint para obter todos os tipos de usuários.
        ---
        tags:
          - Usuario
        responses:
          200:
            description: Lista de tipos de usuários retornada com sucesso
            schema:
              type: array
              items:
                type: string
          404:
            description: Não foi possível obter os tipos de usuários
        """
        resultado = UsuarioController.get_tipos()
        if resultado:
            return jsonify(resultado), 200  # Resposta 200 com o JSON
        else:
            return jsonify({"error": "Não foi possível obter os tipos de usuários"}), 404  # Erro ao buscar tipos
