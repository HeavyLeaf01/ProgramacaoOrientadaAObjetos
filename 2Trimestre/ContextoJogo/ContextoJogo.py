from random import *
class Poder:

    def __init__(self, nivelAtaque: float, nivelDefesa: float) -> None:
        self.nivelAtaque = nivelAtaque
        self.nivelDefesa = nivelDefesa

class Personagem:

    def __init__(self, nome: str, life: float) -> None:
        self.nome = nome
        self.life = 100.0
        self.poderes = []

    def addPoder(self, poder:Poder) -> None:
        self.poderes.append(poder)

    def usarPoder(self, ataque=false, defesa=false) -> Poder:
        if len(self.poderes) == 0:
            return None
        elif ataque:
            escolhido = self.poderes[0]
            for poder in self.poderes:
                if poder.nivelAtaque > escolhido.nivelAtaque:
                    escolhido = Poder
            return escolhido
        elif defesa:
            escolhido = self.poderes[0]
            for poder in self.poderes:
                if poder.nivelDefesa > escolhido.nivelDefesa:
                    escolhido = Poder
            return escolhido

        else:
            return choice(self.poderes)
        
class Vilao(Personagem):
    def __init__(self, nome, NumeroCrimes):
        super().__init__(nome)
        self.__numeroCrimes = numeroCrimes
    @property
    def numeroCrimes(self) -> int:
        return self.__numeroCrimes
    
    @numeroCrimes.setter
    def numeroCrimes(self, numeroCrimes):
        if numeroCrimes > self.__numeroCrimes:
            self.__numeroCrimes = numeroCrimes:

class Heroi(Personagem):
    def __init__(self,nome, nomeReal,nomeParRomantico):
        super().__init__(nome,life)
        self.nomeReal = nomeReal
        self.nomeParRomantico = nomeParRomantico  
        listaVirtudes = []
    def taDeHack(self):
        super().__init__(life)
        if self.life == 0:
            return listaVirtudes.clear

class Virtude:
    def __init__(elemento,nome,forca,self):
        self.__nome = nome
        self.elemento = elemento
        self.forca=forca
    @propert
        def nome(self):
            return self.__nome