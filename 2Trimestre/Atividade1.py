class Jogador:

    global BID
    BID = 0
    def __init__(self, nome, idade):
        BID += 1
        self.BID = BID
        self.nome = nome
        self.idade = idade

class Time:
    def __init__(self, nome, titulos):
        self.nome = nome
        self.titulos = titulos
        self.listaJogadores = []
        
    def addJogador(self, nome, idade):
        if len(self.listaJogadores) < 11:
            self.listaJogadores += [Jogador(nome, idade)]
        else:
            print("Time completo já.")
    def aptoJogo(self):
        return len(self.listaJogadores) == 11
    def experiencia(self):
        if len(self.listaJogadores) > 0:
            maduros = 0
            for jogador in self.listaJogadores:
                if jogador.idade >= 28:
                    maduros += 1
            return maduros / len(self.listaJogadores)
        else:
            return 0.0