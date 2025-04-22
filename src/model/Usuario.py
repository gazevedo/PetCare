class Usuario:
    def __init__(
        self, _id, _email, _senha, _nome, _telefone, _rua, _numero, _bairro,
        _cidade, _cpf, _lojaId, _tipoId, _status
    ):
        self.id = str(_id)
        self.email = _email
        self.senha = _senha
        self.nome = _nome
        self.cpf = _cpf
        self.telefone = _telefone
        self.rua = _rua
        self.numero = _numero
        self.bairro = _bairro
        self.cidade = _cidade
        self.loja = _lojaId
        self.tipo = _tipoId
        self.status = _status

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data.get('_id'),
            _email=data.get('email'),  # ou 'login', conforme o campo real
            _senha=data.get('senha'),
            _nome=data.get('nome'),
            _telefone=data.get('telefone'),
            _rua=data.get('rua'),
            _numero=data.get('numero'),
            _bairro=data.get('bairro'),
            _cidade=data.get('cidade'),
            _cpf=data.get('cpf'),
            _lojaId=data.get('loja'),
            _tipoId=data.get('tipo'),
            _status=data.get('status'),
        )
