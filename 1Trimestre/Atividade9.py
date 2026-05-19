class Corretor:
    def __init__(self, CPF:str, nome:str,comissoes:float) -> None:
        self.CPF = CPF
        self.nome = nome
        self.comissoes = comissoes

    def registroVenda(self,numReg:int) -> bool:   
        pass

class Imobiliaria:
    def __init__(self, CNPJ:str, nome:str, lista:list) -> None:
        self.CNPJ = CNPJ
        self.nome = nome
        if len(lista) < 3:
            print("Imobiliároa deve ter, pelo menos 3 corretores. ")
        else:
            self.listaCorretores = lista
    def addCorretor(self, funcionario:Corretor) -> None:
        self.listaCorretores +=[funcionario] # .append(funcionario)