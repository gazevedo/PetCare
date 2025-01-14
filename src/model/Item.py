class Item:
    def __init__(self, _id, _valor, _produtos):
        self.id = _id
        self.valor = _valor
        self.produtos = _produtos if _produtos is not None else []

    def __str__(self):
        return f"Item(id={self.id}, valor={self.valor}, produtos={self.produtos})"
