class Veiculo:
    def __init__(self, placa, cor):
        self.placa = placa
        self.cor = cor


class Carro(Veiculo):
    def __init__(self, pl, cr, nf, pr):
        super().__init__(pl, cr)
        self.__nomeFornecedor = nf
        self.__preco = pr

    @property
    def nomeFornecedor(self):
        return self.__nomeFornecedor

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        if preco > self.__preco:
            self.__preco = preco


print("Cadastro de Veículos\n")
Veiculos = {}
while input("Realizar cadastro?") in "Ss":
    placa = input("Placa: ")
    cor = input("Cor: ")
    if input("É um carro?") in "Ss":
        nf = input("Qual fornecedor? ")
        pr = float(input("E o preço? "))
        Veiculos[placa] = Carro(placa, cor, nf, pr)
    else:
        Veiculos[placa] = Veiculo(placa, cor)

for v in Veiculos.keys():
    tipo = type(Veiculos[v])
    print(f"{v} -> {tipo}")