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

class Atividade:
    def __init__(self, codigo, descricao, valor):
        self.codigo = codigo
        self. descricao = descricao
        self.valor = valor

class Estudante(Pessoa):
    def __init__(self, CPF:str, nome:str, RA:str):
        super().__init__(CPF, nome)
        self.RA = RA
        self.listaAtividades = []
    def addAtividades(self.atv:Atividade):
        self.listaAtividades.append(atv)