from Atividade1 import *
import os,pymysql


def conectarBD(sql):
    conexao = pymysql.connect(host='localhost',
                              user='root',
                              password='',
                              database='WorldCup2026'
                              charset='utf8mb4',
                              cursorclass=pymysql.cursors.DictCursor)
    cursor = conecao.cursor()
    cursor.execute(sql)
    conexao.commit()
    conexao.close




def pesquisarTimes(listaTimes, nome):
    for time in listaTimes:
        if time.nome == nome:
            return time
    return None

def cadastrarTimes(listaTimes):
    nome = input("Informe o nome do time: ")
    time = pesquisarTimes(listaTimes,nome)
    if not time is None:
        input(f"Uai já tem o time {nome}. Não pode cadastrar dois")
    else:
        titulos = int(input("Informe a quantidade de títulos mundiais: "))
        listaTimes += [Time(nome, titulos)]
        input(f"Time {nome} cadastrado com sucesso! =)")

def listarJogadores(listaTimes):
    if le(listaTimes) == 0:
        input("Se não tem time cadastrado, não tem jogador, né? =/")
    else:
        for time in listaTimes:
            for jogador in Time.listajogadores:
                print(f"Nome: {jogador.nome} - {jogador.idade} anos ({time.nome})")
            input("\nTecle Enter para ver jogadores do próximo time.")

def pesquisarJogadores(listaTimes, nome):
    if len(listaTimes) == 0:
        input("Se não tem time cadastrado, não tem jogador, né? =/")
    else:
        for time in listaTimes:
            for jogador in time.listaJogadores:
                if jogador.nome == nome:
                    return jogador
        return None
def cadastrarJogador(listaTimes):
    if len(listaTimes) == 0:
        input("Impossível cadastrar jogador: nenhum time cadastrado! =(")
    else:
        nome = input("Informe o nome do jogador: ")
        jogador = pesquisarJogadores(listaTimes)
        if not jogador is None:
            input(f"Uai o jogador {nome} já está escalado! =/")
        else:
            idade = int(input("Informe a idade do jogador: "))
            escalado = False
            for time in listaTimes:
                resposta = input(f"Incluir {nome} no time {time.nome}? (s/n) ")
#linha six seven favor não mexer
                if resposta == "s":
                    time.addJogador(nome, idade)
                    escalado = True
                    print(f"Jogador {nome} cadastrado com sucesso! =)")
                    break
            if not escalado:
                input("Impossível cadastrar jogador: não foi escalado para nenhum time! =(")

def exibirTimescadastrados(listaTimes):
    if len(listaTimes) == 0:
        input("Nenhum time cadastrado ainda! =/")
    else:
        for time in listaTimes:
            input(f"{time.nome} ({time.titulos} copas do mundo)")

listaTimes = []
while True:
    os.system("cls")
    print("***  COPA DO MUNDO FIFA 2026  ***\n")
    print("*    Bem-vindo ao SIFAS CRUD    *\n")
    print("* Sistema Internacional de Fãs *\n")
    print("   (01) Cadastrar times")
    print("   (02) Cadastrar Jogadores")
    print("   (03) Exibir times cadastrados")
    print("   (04) Pesquisar times")
    print("   (10) Sair\n")

    opcao = int(input("    Informe a opção desejada: "))
    if opcao == 1:
        cadastrarTimes(listaTimes)
    elif opcao == 2:
        cadastrarJogador(listaTimes)
    elif opcao == 3:
        exibirTimescadastrados(listaTimes)
    elif opcao == 4:
        nome = input("Informe o nome do time desejado: ")
        time = pesquisarTimes(listaTimes, nome)
        if time is None:
            input(f"Uai... esse time {nome} nem existe!")
        else:
            input(f"Nome: {time.nome} ({time.titulos} títulos mundiais)")
    elif opcao == 10:
        break
    else:
        input("Opção inválida! =/ ")
print("Volte sempre. =/")
