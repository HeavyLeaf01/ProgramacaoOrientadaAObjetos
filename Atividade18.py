class Estudante:
    def __init__(self, RA: str, nome: str, area: str):
        self.RA = RA
        self.nome = nome
        self.idade = idade
    
class professor:
    def init(self, CPF: str, nome: str, area: str):    
        self.CPF = CPF
        self.nome = nome
        self.area = area
        self.orientandos = []
    def addEstudante(self, objEstudante):
        self.orientados += [objEstudante]

    def deMenor(self):
        achou = False
        for estudante in self.orientandos:
            if estudante.idade < 18:
                achou = True
                print(f"Ra: {estudante.RA} - Nome: {estudante.nome}")
            if not achou:
                print("Você não orienta estudantes menores de idade.")
