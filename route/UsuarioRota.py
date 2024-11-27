from flask import Blueprint, request
from controller.UsuarioController import UsuarioController

# Criar um Blueprint para as rotas de usuário
usuario_bp = Blueprint('usuario', __name__)

# Instância do controlador
usuario_controller = UsuarioController()


@usuario_bp.route('/usuario', methods=['POST'])
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
    usuario_data = request.get_json()
    return usuario_controller.criar_usuario(usuario_data)
