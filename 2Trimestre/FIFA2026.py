from Atividade1 import *
import os

def cadastrarTimes(listaTimes):
    nome = input("Informe o nome do time: ")
    titulos = int(input("Informe a quantidade de títulos mundiais: "))
    listaTimes += [Time(nome, titulos)]
    print(f"Time {nome} cadastrado com sucesso! =)")

def cadastrarJogador(listaTimes):
    if len(listaTimes) == 0:
        print("Impossível cadastrar jogador: nenhum time cadastrado! =()")
    else:
        nome = input("Informe o nome do jogador: ")
        idade = int(input("Informe a idade do jogador: "))
        escalado = False
        for time in listaTimes:
            resposta = input(f"Incluir {nome} no time {time.nome}? (s/n) ")
            if resposta == "s":
                time.addJogador(nome, idade)
                escalado = True
                print(f"Jogador {nome} cadastrado com sucesso! =)")
                break
        if not escalando:
            print("Impossível cadastrar jogador: não foi escalado para nenhum time! =(")

def exibirTimescadastrados(listaTimes):
    if len(listaTimes) == 0:
        print("Nenhum time cadastrado ainda! =/")
    else:
        for time in listaTimes:
            print(f"{tme.nome} ({time.titulos} copas do mundo)")

listaTimes = []
while True:
    os.system("cls")
    print("***  COPA DO MUNDO FIFA 2026  ***\n")
    print("*    Bem-vindo ao SIFAS CRUD    *\n")
    print("* Sistema Internacional de Fãs *\n")
    print("   (01) Cadastrar times")
    print("   (02) Cadastrar Jogadores")
    print("   (03) Exibir times cadastrados")
    print("   (10) Sair")

    opcao = int(input("    Informe a opção desejada: "))
    if opcao == 1:
        cadastrarTimes(listaTimes)
    elif opcao == 2:
        cadastrarJogador(listaTimes)
    elif opcao == 3:
        exibirTimescadastrados(listaTime)
    elif opcao == 10:
        break
    else:
        input("Opção inválida! =/ ")
print("Volte sempre. =/")
