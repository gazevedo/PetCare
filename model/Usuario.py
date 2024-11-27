import os


class Usuario:
    def __init__(self, id, login, senha, nome, telefone, rua, numero, bairro, cidade, loja, tipo, status):
        self.id = id
        self.login = login
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.loja = loja
        self.tipo = tipo
        self.status = status

    def to_object(self, usuario_data):
        """
                Construtor que aceita um dicionário e automaticamente cria os atributos da classe.
                """
        # Atribui diretamente as chaves do dicionário aos atributos da classe
        for key, value in usuario_data.items():
            setattr(self, key, value)
        return self

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('_')}

