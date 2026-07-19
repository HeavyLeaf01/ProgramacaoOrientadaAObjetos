from Contas import *
import os

if __name__ == "__main__":
    print("Bem-vindo ao Bank POOdle\n")
    while True:
        print("(1) Cadastrar uma nova carteira")
        print("(2) Listar as contas de uma carteira existente")
        print("(3) Sair do programa\n")
        opcao = int(input("Informe a opção desejada: "))

        if opcao == 1:
            inv = input("Qual o tipo de investimento? ")
            car = Carteira(inv)
            resposta = input("Deseja cadastrar uma conta? (s/n) ")
            while resposta == "s":
                num = input("Informe o número da conta: ")
                tit = input("Informe o nome do titular: ")
                sld = float(input("Qual o valor do saldo inicial? "))
                tip = input("Conta normal (N), Conta Corrente (C) ou Conta Poupança (P)? ")
                if tip == "N":
                    car.addConta(Conta(num, tit, sld))
                elif tip == "C":
                    car.addConta(ContaCorrente(num, tit, sld, lim))
                else:
                    ren = float(input("Qual o rendimento mensal? "))
                    car.addConta(ContaPoupanca(num, tit, sld, rend))
                resposta = input("Deseja cadastrar outra conta? (s/n) ")
                listaCarteiras += [car]

            listaCarteiras += [car]
            print(f"Cadastro da carteira {inv} realizado com sucesso! =)\n")
        elif opcao == 2:
            inv = input("Informe o investimento: ")
            for carteirinha in listaCarteiras:
                if carteirinha.investimento == inv:
                    achou = True
                    if carteirinha.listaContas == []:
                        print("Essa carteira " + inv + " não possui contas cadastradas!\n")
                    else:
                        for continha in carteirinha.listaContas:
                            print(continha.retornaDados())
            if not achou:
                print("Não existe carteira do tipo informado! =(")
            else:
                print("Carteira não encontrada! >=/ \n")
        elif opcao == 3:
            break
        else:
            print("Opção inválida! >=/ \n")
        input()
        os.system("cls" if os.name == "nt" else "clear")
    print("Volte sempre ao Bank POOdle")