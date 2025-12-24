# Agregar el atributo hambre, que va a tener un valor entre 0 y 5. 0 es no hambriento, 
# 5 es muy hambriento. Cuando se crea, arranca en nivel 3. Crear un método de instancia alimentar, 
# que reciba una cantidad de comida y disminuya el hambre en esa cantidad. Si el hambre llega a 0, imprimir "Estoy lleno!".

class Perro:
    def __init__(self, color, nombre, raza):
        self.color=color
        self.nombre=nombre
        self.raza=raza
        self.edad=0
        self.hambre=3
    
    def atributos(self):
        print(f"Nombre: {self.nombre}, Color: {self.color}, Raza: {self.raza}, Edad: {self.edad}, Hambre: {self.hambre}")

    def felizCumple(self):
        self.edad+=1

    def alimentar(self, comida):
        if comida>=self.hambre:
            self.hambre=0
            print("Estoy lleno!")
        else:
            self.hambre-=comida


perro=Perro("Beige", "Toto", "Bulldog")
print(perro.atributos())
perro.alimentar(5)
print(perro.atributos())