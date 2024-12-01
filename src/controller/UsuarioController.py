import re

class UsuarioController:
    @staticmethod
    def validar_email(email):
        """
        Função para validar se o email está no formato correto.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))

    @classmethod
    def validar_cadastro_inicial(cls, usuario_data):
        pass
