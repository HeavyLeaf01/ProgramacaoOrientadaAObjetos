from random import *

def realizaCadastro(vetor, coisa, dados):
    vetor = []
    resposta = input(f"Cadastrar {coisa}? (s/n) ")
    while resposta == "s":
        informacoes = []
        for dado in dados:
            tipo = dado[1] if type(dado) == list else str
            informacoes += [tipo(input(f"Informe {dado[0] if type(dado) == list else dado}: "))]
        vetor += [informacoes]
        print("Cadastrado com sucesso!\n")
        resposta = input(f"Cadastrar {coisa}? (s/n) ")


while True:
    clientes = []
    realizaCadastro(clientes,"cliente", ["CPF", "nome", "idade", "endereco"])
    
    brindes = []
    realizaCadastro(brindes, "brinde", ["código", "descrição"])
            
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