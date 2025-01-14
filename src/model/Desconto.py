from datetime import datetime


class Desconto:
    def __init__(self, _id, _lojaID, _quantidade, _utilizado, _tipoId, _dtInicial, _dtFinal):
        """
        Inicializa um objeto Desconto com os atributos fornecidos.

        :param _id: Identificador único do desconto.
        :param _lojaID: Identificador da loja associada ao desconto.
        :param _quantidade: Quantidade de descontos disponíveis.
        :param _quantidade_utilizado: Quantidade de descontos já utilizados.
        :param _tipoId: Identificador do tipo de desconto.
        :param _data_inicial: Data de início da validade do desconto.
        :param _data_final: Data final de validade do desconto.
        """
        self.id = _id
        self.lojaID = _lojaID
        self.quantidade = _quantidade
        self.quantidade_utilizado = _utilizado
        self.tipoId = _tipoId
        self.data_inicial = _dtInicial  # A data deve ser um objeto datetime
        self.data_final = _dtFinal  # A data deve ser um objeto datetime

    def __str__(self):
        """
        Retorna uma representação amigável do objeto como string.
        """
        return (f"Desconto(id={self.id}, lojaID={self.lojaID}, quantidade={self.quantidade}, "
                f"quantidade_utilizado={self.quantidade_utilizado}, tipoId={self.tipoId}, "
                f"data_inicial={self.data_inicial.strftime('%Y-%m-%d')}, data_final={self.data_final.strftime('%Y-%m-%d')})")
