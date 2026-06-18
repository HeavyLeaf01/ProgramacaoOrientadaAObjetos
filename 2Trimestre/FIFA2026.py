from Basedados import *
import os,pymysql

def conectaBD(sql):
    conexao = pymysql.connect(host='localhost',
                            user ='root',
                            password='',
                            database='WoldCup2026',
                            charset ='utf8mb4',
                            cursorclass='pymysql.cursors.DictCursor')
    cursor = conexao.cursor()
    cursor.execute(sql)
    conexao.commit()
    conexao.close()

def PesquisarTimes(listaTimes,BID):
    for time in listaTimes:
        if time.nome == nome:
            return time
        else:
            for time in listaTimes:
                for jogador in time.listaJogadores:
                    if jogador.BID== BID:
                        return jogador
            return None
def PesquisarTimesPorNome(listaTimes,nome):
    for time in listaTimes:
        if time.nome == nome:
            return time
        else:
            for time in listaTimes:
                for jogador in time.listaJogadores:
                    if jogador.nome== nome:
                        return jogador
            return None           
               
def atualizarTimes(listaTimes,nome):
    for i in range(0,len(listaTimes)):
        if listaTimes[i].nome ==nome:
            listaTimes[i].titulos = titulos
            return True
    return False

def CadastrarTime(listaTimes):
    nome = input("Informe o nome do time:")
    time = PesquisarTimes(listaTimes,nome)
    if not time is None:
        print(f"UAI...Ja tem o time {nome}.Não pode cadastrar dois =/")
    else:
        titulos = int(input("Informe a quantidade de titulos mundiais: "))
        listaTimes += [Time(nome,titulos)]
        conectaBD(f"insert into Equipe values ('{nome}',{titulo})")
        input(f"{nome} cadastrado com sucesso! =)")
def listarJogador(listaTimes):
    if len(listaTimes) == 0:
        input("Se não tem time cadastrado, não tem jogador, né ")
    else:
        for time in listaTimes:
            for jogador in time.listaJogadores:
                print(f"Nome: {jogador.nome} - {jogador.idade} anos ({time.nome})")
            input("\n Tecle Enter para ver jogadores do próximo time.")
#listaDados --> 0 , nome/1-idade-time escalado
def atualizarJogadores(listaTimes,nome,listaDados):
    atualizou = False
           for i in range(0,le(listaTimes)):
                for j inrange(0.len(listaTimes[i].listaJogadores)):
                    if listaTime[i].listaJogadores[j].nome ==nome:
                        if not listaDados[0] is None:
                            listaTimes[i].listaJogadores[j].nome== listaDados[0]
                            atualizou =True
                    if not listaDados[1]is None:
                        listaTimes[i].listaJogadores[j].idade== listaDados[1]
                        atualizou =True
                        #Falta atualizar em qual time será reescalado
                        if not listaDados[2]is None:
                            jogadorReserva = listaTimes[i].listaTimes[j]
                            listaTimes[i].listajogadores[j]=None
                            for k in range(0,len(listaTimes)):
                                if listaTimes[k].nome==listaDados[2]:
                                    listaTimes[k].addJogador(nome,jogadorReserva.idade)
                            listaTimes[i].listaJogadores = [
                                jogadorMantido
                                for jogadorMantido in listaTimes[i].listaJogadores
                                if not jogadorMantido is None
                            ]
                            atualizou =True
            return atualizou
    return atualizou
     
            

def CadastrarJogador(listaTimes):
    if len (listaTimes) == 0:
        print("Impossivel cadastrar jogador! =(")
    else:
        nome = input("Informe o nome do jogador: ")
        jogador =  PesquisarTimesPorNome(listaTimes,nome)
        if jogador is None:
            input(f"UAI...O jogador {nome} já está escalado!")
        else:  
            idade = int(input("Informe a idade do jogador: "))
            escalado = False
            for time in listaTimes:
                resposta = input(f"Incluir {nome} no time {time.nome}? (s/n)")
                if resposta == "s":
                    time.addJogador(nome,idade)
                    escalado = True
                    print(f"Jogador {nome} cadastrado com sucesso! =)")
                    break
        if not escalado:
            print("Impossivel cadastrar jogador: nao foi escalado para nenhum time! =(")
def exibirTimesCadastrados(listaTimes):
    if len(listaTimes) ==0:
        print("Nenhum time cadastrado ainda! =/")
    else:
        for time in listaTimes:
            print(f"{time.nome}({time.titulos} copa do mundo)")


global cursor
cursor = conexao.cursor()
listaTimes =[]
while True:
    os.system("cls")
    print("***      COPA DO MUNDO FIFA 2026 ***\n")
    print("*        Bem-vindo ao SIFAS CRUD  *\n")
    print("*   Sistema Internacional de Fãs *\n)")
    print("(01) Cadastrar time")
    print("(02) CAdastrar jogador")
    print("(03) Exibir times cadastrados")
    print("(04) Pesquisar Times")
    print("(05) Exibir Jogadores")
    print("(06) Pesquisar jogadores")
    print("(07) Atualizar Times")
    print("(08) Atualizar Jogador")
    print("(10) sair")
    opcao = int(input("Informe a opcão desejada: "))
    if opcao ==1:
        CadastrarTime(listaTimes)
    elif opcao == 2:
        CadastrarJogador(listaTimes)
    elif opcao ==3:
        exibirTimesCadastrados(listaTimes)
    elif opcao == 4:
        nome=input("Imforme o nome do time desejado: ")
        time = PesquisarTimes(listaTimes,nome)
        if time is None:
            input(f"UAI..Esse time {nome} nem existe!")
        else:
            input(f"Nome: {time.nome} ({time.titulos} títulos mundiais)")
    elif opcao ==5:
        exibirjogadores(listaTimes)
    elif opcao == 6:
        BID = int(input("Informe o BID do jogador desejado: "))
        jogador = pesquisarJogador(listaTimes,BID)
        if jogador is None:
            input(f"UAI..Esse time {BID} nem existe!")
        else:
            input(f"Nome: {jogador.nome} ({jogador.titulos} títulos mundiais)")
    elif opcao ==7:
        nome=input("Informe o nome do time desejado")
        titulos = int(input("Informe a nova quantidade de títulos mundiais: "))

        if atualizarTimes(listaTimes,nome,titulos):
            input(f"O time {nome} foi atualizado com sucesso!")
        else:
            input(f"Uai...esse time {nome} nem existe =(")
    elif opcao ==8:
         nome= int(input("Informe o nome do jogador desejado: "))
        jogador = pesquisarJogador(listaTimes,BID)
        if jogador is None:
            input(f"UAI..o jogador do {nome} nem existe!")
        else:
            listaDados =[None,None,None]
            if input(f"Deseja atualizar o nome?(s/n)") =="s":
                listaDados[0] = input("Informe o novo nome:")
            if input(f"Deseja atualizar a idade?(s/n)") =="s":
                listaDados[1] = int(input("Informe a nova idade:"))
            if input("Reescalar o jogador em outro tine(s/n)") == "s":
                listaDados[2] = int(input("Informe outro nome do time:"))
            if atualizarJogadores(listaTimes,nome,listaDados):
                input(f"{jogador.nome} atualizado com sucesso")
            else:
                input(f"UAI..o jogador do {nome} nem existe!")

    elif opcao ==10:
        break
    else:
        input("Opção inválida! =\ ")
print("Volte sempre =)")