class UsuarioTipo:
    def __init__(self, _id, _descricao, _tipo):
        """
        Inicializa um objeto UsuarioTipo com os atributos id e descricao.

        :param id: Identificador único do tipo de usuário (inteiro).
        :param descricao: Descrição do tipo de usuário (string).
        """
        self.id = str(_id)
        self.descricao = _descricao
        self.tipo = _tipo
