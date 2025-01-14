class Plano:
    def __init__(self, _id, _lojaId, _valor, _descricao, _titulo, _status):
        """
        Inicializa um objeto Plano com os atributos fornecidos.

        :param _id: Identificador único do plano.
        :param _lojaid: Identificador da loja associada ao plano.
        :param _valor: Valor do plano.
        :param _descricao: Descrição do plano.
        :param _titulo: Título do plano.
        :param _status: Status do plano (ativo, inativo, etc).
        """
        self.id = _id
        self.lojaId = _lojaId
        self.valor = _valor
        self.descricao = _descricao
        self.titulo = _titulo
        self.status = _status

    def __str__(self):
        """
        Retorna uma representação amigável do objeto como string.
        """
        return (f"Plano(id={self.id}, lojaid={self.lojaId}, valor={self.valor}, "
                f"descricao='{self.descricao}', titulo='{self.titulo}', status='{self.status}')")
