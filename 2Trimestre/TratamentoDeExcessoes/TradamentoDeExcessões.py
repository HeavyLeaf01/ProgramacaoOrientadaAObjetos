from random import *

while True:
    try:
        q = int(input("Até quantas caixas? "))
        break
    except:
        print("Valor indivídual!")
n = randint(1,q)
inicio = Caixa(1,None)
final = inicio
for numero in range(2,n):
    final.setinha = Caixa(numero,None)
    final = final.setinha