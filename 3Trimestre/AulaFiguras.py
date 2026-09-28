from abc import *
import math

class Figura2D(ABC):
    def __init__(self, cor: str) -> None:
        self.cor = cor

    @abstractmethod
    def calculadoraArea() -> float:
        pass


class Circulo(Figura2D):
    def __init__(self, cor: str, raio: float) -> None:
        super().__init__(cor)
        self.raio = raio

    def calcularArea(self) -> float:
        return math.pi * (self.raio ** 2)


class Quadrado(Figura2D):
    def __init__(self, cor: str, lado: float) -> None:
        super().__init__(cor)
        self.lado = lado

    def calcularArea(self) -> float:
        return math.pi * (self.raio ** 2)

    def inclinar(self, eixo: str) -> None:
        pass


class Retangulo(Figura2D):
    def __init__(self, cor: str, base: float, altura: float):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        return self.base * self.altura

    def inclinar(self, eixo: str) -> None:
        pass

class Quadrado(Retangulo):
    def __init__(self, cor: str, lado: float) -> None:

        super().__init__(cor, base=lado, altura=lado)
        self.lado = lado