
class Potencia:
    def __init__(self, num):
        self.numero = num
        self.sucessivas = []
    def sequencia(self):
        self.sucessivas += [self.numero ** len(self.sucessivas)]

x = int(input("Informe um número: "))
p = Potencia(x)
y = int(input("Quantas potências? "))
for i in range(y):
    p.sequencia()
print(p.sucessivas)


sucessivas = []

x = int(input("Informe um número: ")) 
y = int(input("Quantas potências? "))
for i in range(y):
    sucessivas += [x ** len(sucessivas)]
print(sucessivas)

