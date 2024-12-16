from bson import ObjectId


class Loja:
    def __init__(
            self, _id, _nome, _telefone, _rua, _numero, _bairro,
            _cidade, _cep, _status):
        self.id = str(_id)
        self.nome = _nome
        self.telefone = _telefone
        self.rua = _rua
        self.numero = _numero
        self.bairro = _bairro
        self.cidade = _cidade
        self.cep = _cep
        self.status = _status

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "rua": self.rua,
            "numero": self.numero,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "cep": self.cep,
            "status": self.status
        }

    @classmethod
    def to_object(cls, data):
        return cls(
            _id=data.get('_id'),
            _nome=data.get('nome'),
            _telefone=data.get('telefone'),
            _rua=data.get('rua'),
            _numero=data.get('numero'),
            _bairro=data.get('bairro'),
            _cidade=data.get('cidade'),
            _status=data.get('status'),
            _cep=data.get('cep')
        )
