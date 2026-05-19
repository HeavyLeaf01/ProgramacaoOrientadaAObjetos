class Corretor:
    def __init__(self, cpf: str, nome: str, comissao: float):
        
        self.cpf = cpf
        self.nome = nome
        self.comissao = comissao

    def registrar_tentativa_venda(self, numero_registro_cartorio):

        if numero_registro_cartorio % 2 == 0:
            print(f"Venda do imóvel {numero_registro_cartorio} realizada com sucesso por {self.nome}!")
            return True
        else:
            print(f"A tentativa de venda do imóvel {numero_registro_cartorio} falhou.")
            return False


