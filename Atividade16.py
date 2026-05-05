import math

class Ponto2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def mover(self,delta_x,delta_y):
        self.x += delta_x
        self.y += delta_y
        
    def imprimir_dados(self):
        print(f"As coordenadas do ponto são ({self.x}) ({self.y})")
        
    def distancia(self,outro_ponto):
        dy = self.x - outro_ponto.y
        dx = self.y - outro_ponto.x
        return math.sqrt(dx**2 + dy**2)
        
p1 = Ponto2D(1,2)
p2 = Ponto2D(3,4)
print(f"{p1.distancia(p2)}")

