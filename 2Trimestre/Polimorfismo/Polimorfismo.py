class Pessoa:
    def __init__(self, nome:str) -> None:
        self.nome = nome
    def exibeDados(self) -> str:
        dados = f"Nome: {self.nome}"
        return dados

class Fisica(Pessoa):
    def __init__(self, nome:str, CPF: str) -> None:
        super().__init__(nome)
        self.CPF = CPF

    def exibeDados(self) -> str:
        dados = super().exibeDados()
        return dados + f" CPF {self.CPF}"
class Juridica(Pessoa):
    def __init__(self, nome: str, CNPJ: str, tipo: str):
        super().__init__(nome)
        self.CNPJ = CNPJ
        self.tipo = tipo
    def exibeDados(self) -> str:
        dados = super().exibeDados()
        return dados + f" {self.tipo}" + f" CNPJ {self.CNPJ}"


nome = input("Informe seu nome: ")
if int(input("Pessoa Física (1) ou Jurídica (2)? ")) == 1:
    doc = input("Informe o seu CPF: ")
    pessoa = Fisica(nome, doc)
else:
    doc = input("Informe o seu CNPJ: ")
    tipo = input("Ltda ou S/A? ")
    pessoa = Juridica(nome, doc, tipo)
print(pessoa.exibeDados())
