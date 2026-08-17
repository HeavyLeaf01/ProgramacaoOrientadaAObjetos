from random import *

def mostraLinha(inicio):
    aux = inicio
    while aux is not None:
        numero = aux.valor
        print(f"| {numero if numero >= 10 else f'0{numero}'} | -->" , end="")
        aux = aux.setinha
    print('[ | | ]')

class Caixa:
    def __init__(self,valor,setinha):
        self.valor = valor
        self.setinha = setinha

#q = int(input("Até quantas caixas? "))
while True:
    try:
        q = int(input("Até quantas caixas? "))
        break
    except:
        print("Valor inválido! ")
        
n = randint(1,q)
inicio = Caixa(1,None)
final = inicio

for numero in range(2,n+1):
    final.setinha = Caixa(randint(0,100),None)
    final = final.setinha
    
mostraLinha(inicio)

numeroAtual = int(input("Qual número quer atualizar? "))
aux = inicio

while aux is not None:
    if aux.valor == numeroAtual:
        aux.valor = aux.valor ** 2
    aux = aux.setinha
mostrarLista(inicio)

























#linha six seven, favor NÃO MEXER!!!!!!!!!!!!!!!!!!!!!!!!!!!!