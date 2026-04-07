from random import *

class Poder:
    def __init__(self, na: float, nd: float) -> None:
        self.nivelAtaque = na
        self.nivelDefesa = nd

class Personagem:
    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__life = 100.0
        self.listaPoderes = []
    @property
    def nome(self) -> str:
        return self.__nome
    @property
    def life(self) -> float:
        return self.__life
    @life.setter
    def life(self, life) -> float:
        if 0 <= life < 100.0:
            self.__life = life
    def addPoder(self, poder:Poder) -> None:
        self.listaPoderes += [poder]
    def usarPoder(self) -> Poder:
        if len(self.listaPoderes) == 0:
            print("Não existem poderes! =(")
            return None
        return choice(self.listaPoderes)