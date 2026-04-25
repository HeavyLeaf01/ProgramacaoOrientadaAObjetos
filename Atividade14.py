class Arma:
    def __init__(self, Nome: str, Tipo: str):
        self.Nome = Nome
        self.Tipo = Tipo
        armaInicial = 'espada de madeira'
class Personagem:
    def __init__(self, Nome: str, Categoria: str):
        self.Nome = Nome
        self.Categoria = Categoria
        espada_de_madeira = Arma('Espada de madeira', 'Física')
        self.Armas = [espada_de_madeira]
    def addArma(self, arma):
        self.Armas.append(arma)
        print(f"Arma '{arma.Nome}' adicionada com sucesso!")        

Gabriel = Personagem('Gabriel', 'Humano')
espada = Arma('Excalibur', 'Física')

Gabriel.addArma(espada)

print(f"Total de armas de {Gabriel.Nome}: {len(Gabriel.Armas)}")
for a in Gabriel.Armas:
    print(f"- {a.Nome}")