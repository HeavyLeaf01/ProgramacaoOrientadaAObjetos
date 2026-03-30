class Professor:
    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao

class Aula:
    def __init__(self, data, horaInicio, horaFinal, professor):
        self.data = data    
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        self.professor = professor