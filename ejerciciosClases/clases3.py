# Crear la clase Circulo, con el atributo radio. Crear el constructor que recibe el radio. 
# Crear un método que calcule el área. Crear un método que calcule el perímetro.

import math

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def area(self):
        return math.pi*(self.radio ** 2)
    
    def perimetro(self):
        return math.pi*(self.radio * 2)
    
circulo=Circulo(5)
print(f"Área del círculo: {circulo.area()}")
print(f"Perímetro del círculo: {circulo.perimetro()}")

# Martu: ¡Muy bien! :)