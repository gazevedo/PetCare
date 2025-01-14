class DescontoTipo:
    def __init__(self, _id, _descricao):
        self.id = _id
        self.descricao = _descricao

    def __str__(self):
        """
        Retorna uma representação amigável do objeto como string.
        """
        return f"DescontoTipo(id={self.id}, descricao='{self.descricao}')"
