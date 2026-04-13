class Fornecedor:
    def __init__(self, CNPJ: str,nome: str):
        self.CNPJ = CNPJ
        self.nome = nome

    def emitirNota(self, di: date, df: date) -> float:
        self.di = di
        self.df = df
class Produto:
    def __init__(self, codigo: int, descricao: str, preco: float):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
class Venda:
    def __init__(self, quantidade: int, dataVenda: date):
        self.quantidade = quantidade
        self.datavenda = dataVenda
        
