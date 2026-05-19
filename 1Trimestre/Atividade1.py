from random import *

while True:
    clientes = []
    resposta2 = input("Cadastrar cliente? (s/m) ")
    while resposta2 == "s":
        cpf = input("Informe o CPF: ")
        nome = input("Informe o nome: ")
        idade = int(input("Informe a idade:"))
        endereco = input("Informe o endereço: ")
        clientes += [[cpf, nome, idade, endereco]]
        print("Cadastrado com sucesso! \n")
        resposta2 = input("Cadastrar cliente? (s/n) ")
        
    brindes = []
    resposta3 = input("Cadastrar cliente? (s/m) ")
    while resposta3 == "s":
        codigo = input("Informe o código: ")
        descricao = input("Informe o descrição: ")
        brindes += [[codigo, descricao]]
        print("Cadastrado com sucesso! \n")
        resposta3 = input("Cadastrar brinde? (s/n) ")
        
    sorteados = {}
    quantos = int(input("Quantos brindes? "))
    for sorteio in range(0, quantos):
        c = choice(clientes)
        b = choice(brindes)
        if not c[0] in sorteados:
            sorteados[c[0]] = b
    for clienteSorteado in sorteados.item():
        print(clienteSorteado)
        
    resposta1 = input("Sair do programa? (s/n) ")
    if resposta1 == "s":
        break