from datetime import datetime

class Assinatura:
    def __init__(self, _id, _planoId, _clienteId, _dataIni, _dataFin):
        """
        Inicializa um objeto Assinatura com os atributos fornecidos.

        :param _id: Identificador único da assinatura.
        :param _planoid: Identificador do plano associado à assinatura.
        :param _clienteid: Identificador do cliente associado à assinatura.
        :param _data_inicio: Data de início da assinatura.
        :param _data_fim: Data de fim da assinatura.
        """
        self.id = _id
        self.planoid = _planoId
        self.clienteid = _clienteId
        self.data_inicio = _dataIni  # A data deve ser um objeto datetime
        self.data_fim = _dataFin        # A data deve ser um objeto datetime

    def __str__(self):
        """
        Retorna uma representação amigável do objeto como string.
        """
        return (f"Assinatura(id={self.id}, planoid={self.planoid}, clienteid={self.clienteid}, "
                f"data_inicio={self.data_inicio.strftime('%Y-%m-%d')}, data_fim={self.data_fim.strftime('%Y-%m-%d')})")
