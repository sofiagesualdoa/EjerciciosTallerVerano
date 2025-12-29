# Rediseñar el ejemplo de Rectángulo y Círculo, porque hay algunos métodos que seguramente 
# sean comunes o tengan alguna parte en común. STR, superficie, perímetro por ejemplo. 
# Tengo que agregar: Cuadrado, Rombo, Polígono, Trapecio. La clase Cuadrado, hereda de 
# Rectángulo? O Rectángulo hereda de Cuadrado? O ninguna de las dos?

from abc import ABC, abstractmethod # Martu: Je, te adelantaste un ejercicio :)
from math import pi

class Polígono(ABC):
    
    @property
    @abstractmethod
    def cantLados(self):
        pass
    
    @abstractmethod
    def superficie(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return "Polígono"

class Circulo():
    def __init__(self, radio):
        self.radio=radio

    def superficie(self):
        return pi*self.radio**2
    
    def perimetro(self):
        return pi*(self.radio*2)
    
    def __str__(self):
        return "Círculo"
    
class Rectangulo(Polígono):
    def __init__(self, ancho, largo):
        self.ancho=ancho
        self.largo=largo

    def superficie(self):
        return self.ancho*self.largo
    
    def perimetro(self):
        return (self.ancho*2)+(self.largo*2)
    
    def __str__(self):
        return "Rectángulo"
    
    @property
    def cantLados(self):
        return 4

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def __str__(self):
        return "Cuadrado"
    
class Rombo(Polígono):
    def __init__(self, lado, diagMayor, diagMenor):
        self.lado=lado
        self.diagMayor=diagMayor
        self.diagMenor=diagMenor

    def superficie(self):
        return (self.diagMenor*self.diagMayor)/2
    
    def perimetro(self):
        return self.lado*4
    
    def __str__(self):
        return "Rombo"

    @property
    def cantLados(self):
        return 4
    
class Trapecio(Polígono):
    def __init__(self, baseMayor, baseMenor, altura, lado1, lado2):
        self.altura=altura
        self.baseMayor=baseMayor
        self.baseMenor=baseMenor
        self.lado1=lado1
        self.lado2=lado2

    def superficie(self):
        return ((self.baseMenor+self.baseMayor)*self.altura)/2
    
    def perimetro(self):
        return self.baseMayor+self.baseMenor+self.lado2+self.lado1
    
    def __str__(self):
        return "Trapecio"
    
    @property
    def cantLados(self):
        return 4
    
# Martu: Muy bien!!! Aunque también podrías hacer una superclase común como "Figura" para que todo el resto de figuras
# hereden esa superclase, ya que, por ejemplo, el círculo no es un polígono. 