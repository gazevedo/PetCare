class Pagamento:
    def __init__(self, _id, _id_caixa, _valor_total, _itens, _id_agenda):
        self.id = _id
        self.id_caixa = _id_caixa
        self.valor_total = _valor_total
        self.itens = _itens  if _itens is not None else []
        self.id_agenda = _id_agenda

    def __str__(self):
        return f"Pagamento(id={self.id}, id_caixa={self.id_caixa}, valor_total={self.valor_total}, itens={self.itens}, id_agenda={self.id_agenda})"
