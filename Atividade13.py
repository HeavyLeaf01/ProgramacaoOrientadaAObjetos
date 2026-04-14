from datetime import date

class Venda:
    def __init__(self, quantidade: int, dataVenda: date, fornecedor, produto):
        self.quantidade = quantidade
        self.datavenda = dataVenda
        self.fornecedor = fornecedor
        self.produto = produto
class Produto:
    def __init__(self, codigo: int, descricao: str, preco: float):
        self.__codigo = codigo
        self.descricao = descricao
        self.__preco = preco
    @property
    def codigo(self):
        return self.__codigo
    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self,preco):
        if preco > self.preco:
            self.preco = preco
class Fornecedor:
    def __init__(self, CNPJ: str,nome: str):
        self.CNPJ = CNPJ
        self.nome = nome
        self.listaVendaProdutos = []

    def addVenda(self, q, datavenda, produto):
        objeto = Venda(self, q, datavenda, produto)
        self.listaVendaProdutos.append(objeto)
    def emitirNota(self, di: date, df: date) -> float:
        soma = 0.0
        for item in self.listaVendaProdutos:
            if di <= item.dataVenda <= df:
                total += (item.quantidade * item.produto.preco)
        return total

identificacao = input("Informe o número do CNPJ da empresa: ")
razaoSocial = input("Informe o nome do fornecedor: ")
empresa = Fornecedor(identificacao, razaoSocial)

quantas = int(input("Quanta vendas realizadas?: "))
for i in range(0,quantas):
    codProd = int(input("Código do produto: "))
    marca = input("Descrição da marca do produto: ")
    preco = float(input("Quanto custa? R$:  "))
    quant = int(input("Quantidade vendida desse produto: "))
    dataV = date(int(input("Ano: ")), int(input("Mês: ")), int(input("Dia: ")))
    empresa.addVenda(quant, dataV, Produto(codProd,marca,preco))
    print(f"Venda cadastrada com sucesso em {dataV.strftime("%d/%m/%Y")}")