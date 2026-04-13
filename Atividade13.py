from datetime import date
class Fornecedor:
    def __init__(self, CNPJ: str,nome: str):
        self.CNPJ = CNPJ
        self.nome = nome
        self.listaVendaProdutos = []

    def addVenda(self, q, dv, p):
        self.listaVendaProdutos.append(Venda(self,q,dv,p))
    def emitirNota(self, di: date, df: date) -> float:
        pass

class Produto:
    def __init__(self, codigo: int, descricao: str, preco: float):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco
class Venda:
    def __init__(self, quantidade: int, dataVenda: date, fornecedor, produto):
        self.quantidade = quantidade
        self.datavenda = dataVenda

