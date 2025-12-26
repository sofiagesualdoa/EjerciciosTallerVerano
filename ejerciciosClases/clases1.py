# Crear la clase Perro, con los atributos color, nombre, edad, raza.
# Crear el constructor que recibe color, nombre y raza. La edad por defecto es 0.
# Crear un método que imprima todos los atributos.
# Crear un método de instancia felizCumple, que aumenta la edad en 1.

class Perro:
    def __init__(self, color, nombre, raza):
        self.color=color
        self.nombre=nombre
        self.raza=raza
        self.edad=0
    
    def atributos(self): # Martu: Muy bien! También podrías definir el método __str__
        print(f"Nombre: {self.nombre}, Color: {self.color}, Raza: {self.raza}, Edad: {self.edad}")

    def felizCumple(self):
        self.edad+=1

perro=Perro("Beige", "Toto", "Bulldog")
print(perro.atributos())
perro.felizCumple()
print(perro.atributos())

# Martu: Muy bien!!
