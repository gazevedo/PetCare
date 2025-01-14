class MovimentacaoTipo:
    """
    Representa o tipo de movimentação (e.g., entrada, saída).
    """
    def __init__(self, _id, _descricao):
        self.id = str(_id)
        self.descricao = _descricao