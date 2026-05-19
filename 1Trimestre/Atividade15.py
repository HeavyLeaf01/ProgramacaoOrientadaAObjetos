class Filme:
    def __init__(self, titulo, ano) -> None:
        self.titulo = titulo
        self.ano = ano
        self. avaliacoes = []
    def avaliar(self, nota) -> None:
        self.avaliacoes += [nota]
    def imprimirMedia(self) -> None:
        media = sum(self.avaliacoes) / len(self.avaliacoes)
        print(f"{media}")
