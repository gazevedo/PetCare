import os

class Usuario:
    def __init__(
            self, login, senha, nome=None, telefone=None, rua=None, numero=None, bairro=None,
            cidade=None, cpf=None, loja=None, tipo=None, status=None):
        self.login = login
        self.senha = senha
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.loja = loja  # Pega o valor da variável de ambiente
        self.tipo = tipo  # Tipo padrão do usuário
        self.status = status  # Usuário ativo por padrão

    def to_dict(self):
        """
        Converte a instância do usuário para um dicionário.

        :return: Dicionário com os dados do usuário.
        """
        return {
            "login": self.login,
            "senha": self.senha,
            "nome": self.nome,
            "cpf": self.cpf,
            "telefone": self.telefone,
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "loja": self.loja,
            "tipo": self.tipo,
            "status": self.status
        }

    @classmethod
    def to_object(cls, usuario_data):
        """
        Converte um dicionário de volta para uma instância de Usuario.

        :param usuario_data: Dicionário com dados do usuário.
        :return: Instância de Usuario.
        """
        return cls(
            login=usuario_data.get('login'),
            senha=usuario_data.get('senha'),
            nome=usuario_data.get('nome'),
            cpf= usuario_data.get('cpf'),
            telefone=usuario_data.get('telefone'),
            rua=usuario_data.get('rua'),
            numero=usuario_data.get('numero'),
            bairro=usuario_data.get('bairro'),
            cidade=usuario_data.get('cidade'),
            loja= usuario_data("loja"),
            tipo= usuario_data("tipo"),
            status= usuario_data("status"),

        )
