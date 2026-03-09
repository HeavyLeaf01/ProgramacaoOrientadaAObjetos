#Modularização e teoria da Recursividade
#-Definição de funções e controle de chamadas
#-Passo Base => if de parada/ignore
#-Passo Recursivo => comportamento padrão para elemento adjacente
#-Casos de código mais simples x sobrecarga CPU
#Exemplo 1 => Somatória (+fácil)

#      n
#______________
#\
# \
#  \
#  /
# /                 i = 1 + 2 + 3 + 4 + 5 = 15                                  
#_______________
#      i = 1
numero = int(input("Digite um número: "))
def somatorio(n):
    total = 0
    for i in range(1,n+1):
        total = total + i
    return total


print(f"Somatório = {somatorio(numero)}")


def somarecursiva(n):
    if n < 1:
        return 0
    else:
        return n + somaRecursiva(n-1)




#Exemplo 2 => Produto :
#           n
#______________________
#   |               |
#   |               |
#   |               |
#   |               |
#   |               |        i    0   1   2   3   4
#   |               |       2  = 2 . 2 . 2 . 2 . 2
#   |               |
#   |               |
#   |               |
#   |               |
#       i = 0

def produtorio(n):
    if n == 0:
        return 1
    return 2**n * produtorio(n-1)





#Exemplo 3 => Sequência de Fibonacci


#0, 1, 1, 2, 3, 5, 8, 13, 21, 33 ...

def  fibonacci(n):
    if n == 1:
        return 0
    
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
for i in range(1, numero + 1):
    print(fibonacci(i))



