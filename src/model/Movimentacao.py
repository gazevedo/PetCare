from src.model.Caixa import Caixa
from src.model.MovimentacaoTipo import MovimentacaoTipo


class Movimentacao:
    """
    Representa uma movimentação no caixa.
    """
    def __init__(self, _id, _data, _valor,  _tipoId):
        self.id = str(_id)
        self.data = _data
        self.tipo = _tipoId
        self.valor = _valor