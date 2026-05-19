from Atividade9 import *

def cadastroCorretor(listaCorretores:list) -> None:
    print("CADASTRO DE CORRETORES\n")
    while True:
        CPF = input("Informe o CPF do corretor: ")
        nome = input("Nome do corretor: ")
        comissao = float(input("Valor a receber de comissões: "))
        servidor = Corretor(CPF, nome, comissao)
        listaCorretores += [ servidor]
        print("Corretor cadastrado com sucesso! = \n")
        resposta = input("Deseja continuar? (s/n) ")
        if resposta == "n":
            break
    def listagemCorretor(listaCorretores:list) -> None:
        print("LISTAGEM DE CORRETORES\n")
        for corretor in listaCorretores:
            print(f"{corretor.nome} (R${corretor.comissoes})")

    def cadastraImobiliaria(imobiliarias:list, listaCorretores:list) -> None:
        print("CADASTRO DE IMOBILIÁRIAS\n")
        while True:
            CNPJ = input("Informe o CNPJ da imobiliária: ")
            nome = input("Nome da imobiliária: ")
            listaEmpregados = []
            for corretor in istaCorretores:
                adiciona = input(f"Empregar o corretor {corretor.name}? (s/n)")
                if adiciona == "s":
                    listaEmpregados += [corretor]
                    empresa = Imobiliaria(CNPJ, nome, listaEmpregados)
                    print("Imobiliaria cadastrada com sucesso! (Será? rs)")
                    resposta = input("Deseja continuar? (s/n) ")
                    if resposta == "n":
                        break