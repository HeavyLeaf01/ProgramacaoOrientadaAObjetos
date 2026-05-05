class Aluno:
    def __init__(self):
        pass
class Professor:
    def __init__(self):
        self.alunos = []
    def addAlunos(self, aluno):
        self.alunos.append(aluno)