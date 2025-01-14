class Agenda:
    def __init__(self, _id, _lojaId, _clienteId, _atendenteId, _data, _status, _produtos):
        self.id = _id
        self.loja = _lojaId
        self.cliente = _clienteId
        self.atendente = _atendenteId
        self.data = _data
        self.status = _status
        self.produtos = _produtos if _produtos is not None else []
