# src/controller/UsuarioController.py

import re

class UsuarioController:

    @staticmethod
    def validar_email(email):
        """
        Valida se o email fornecido está no formato correto.
        """
        regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(regex, email))
