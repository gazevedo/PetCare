from src.model.MovimentacaoTipo import MovimentacaoTipo

class Caixa:
    """
    Representa o caixa de uma loja.
    """
    def __init__(self, _id, _lojaID, _usuarioId, _movimentacoes):
        self.id = _id
        self.lojaID = _lojaID
        self.usuarioId = _usuarioId
        self.movimentacoes = _movimentacoes if _movimentacoes is not None else []

