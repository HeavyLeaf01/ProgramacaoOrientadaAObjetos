from Componentes import Pneu

class Carro:
    def __init__(self, placa: str, cor: str, preco: float) -> None:
        self.placa = placa
        self.cor = cor
        self.preco = preco
        self.listaPneus = []
    def addPneu(self, marca: str, aro: int) -> None:
        self.listaPneus += [Pneu(marca, aro)]

placa = input("Informe a placa: ")
cor = input("Vai ser de qual cor o carro? ")
preco = float(input("Valor em R$ "))
carango = Carro(placa,cor,preco)
marca, aro = input("Marca do pneu: "), int(input("E o aro? "))
for pneu in range(0, 4):
    carango.addPneu(marca,aro)
print("Seu carango cabuloso cadastrado com sucesso! >=)")
    