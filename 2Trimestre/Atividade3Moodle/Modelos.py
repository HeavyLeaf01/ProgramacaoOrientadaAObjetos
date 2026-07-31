import random

class Poder:
    def __init__(self, nivelAtaque, nivelDefesa):
        self.__nivelAtaque = nivelAtaque
        self.__nivelDefesa = nivelDefesa

    @property
    def nivelAtaque(self):
        return self.__nivelAtaque

    @property
    def nivelDefesa(self):
        return self.__nivelDefesa

class Virtude:
    def __init__(self, nome, elemento, forca):
        self.__nome = nome
        self.__elemento = elemento
        self.__forca = forca

    @property
    def nome(self):
        return self.__nome

class Personagem:
    def __init__(self, nome, life):
        self.__nome = nome
        self.__life = life
        self.__poderes = []

    @property
    def nome(self):
        return self.__nome

    @property
    def life(self):
        return self.__life

    @life.setter
    def life(self, valor):
        self.__life = valor

    def addPoder(self, objetoPoder):
        self.__poderes += [objetoPoder]

    def usarPoder(self):
        if self.__poderes != []:
            return random.choice(self.__poderes)
        return Poder(0.0, 0.0)

class Heroi(Personagem):
    def __init__(self, nome, life, nomeReal, nomeParRomantico):
        super().__init__(nome, life)
        self.__nomeReal = nomeReal
        self.__nomeParRomantico = nomeParRomantico
        self.__virtudes = []

    def addVirtude(self, objetoVirtude):
        self.__virtudes += [objetoVirtude]

    def taDeHack(self):
        print("\n[HACK ATIVADO] " + self.nome + " usou código de trapaça e recuperou a vida toda! =)")
        self.life = 100.0

class Vilao(Personagem):
    def __init__(self, nome, life, numeroCrimes):
        super().__init__(nome, life)
        self.__numeroCrimes = numeroCrimes