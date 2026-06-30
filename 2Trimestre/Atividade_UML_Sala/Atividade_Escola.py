from datetime import date

class Pessoa:
    def __init__(self,CPF: str, nome: str):
        self.CPF = CPF
        self.nome = nome
        ListaPresenca = []
    def addPresenca(self, ID: int, data:date) ->None:
        self.listaPresenca.append(Presenca(ID,data))

class Docente(Pessoa):
    def __init__(self,CPF,nome,salario):
        super().__init__(CPF,none)
        self.salario = salario

class Estudante(Pessoa):
    def __init__(self, CPF:str, nome:str, RA:str):
        super().__init__(CPF, nome)
        self.RA = RA
        self.listaAtividades = []


class Atividade:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self. descricao = descricao
        self.valor = valor
    def addAtividades(self.atv:Atividade):
        self.listaAtividades.append(atv)

realizacoes = []
def addRealizacoes(self,realizacao):
    self.realizacoes.append(realizacao)
class Realiza:
    def __init__(self, est, atv):
        self.estudante = est
        self.atividade = atv
        self.nota = 0.0
        self.estudante.addRealizacao(self)
        self.atividade.addRealizacao(self)
    def relatorio(self):
        print(f"Estudante: {self.estudante.nome}")
        print(f"{self.atividade.codigo} = {self.nota} pontos")

