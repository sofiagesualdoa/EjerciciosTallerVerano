# Para el ejercicio 1, agregar una clase abstracta Figura y llevar todo el 
# comportamiento posible a esa clase.

from abc import ABC, abstractmethod
from math import pi

class Figura(ABC):

    @abstractmethod
    def superficie(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __str__(self):
        return self.__class__.__name__

class Polígono(Figura):
    
    @property
    @abstractmethod
    def cantLados(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio=radio

    def superficie(self):
        return pi*self.radio**2
    
    def perimetro(self):
        return pi*(self.radio*2)
    
class Rectangulo(Polígono):
    def __init__(self, ancho, largo):
        self.ancho=ancho
        self.largo=largo

    def superficie(self):
        return self.ancho*self.largo
    
    def perimetro(self):
        return (self.ancho*2)+(self.largo*2)
    
    @property
    def cantLados(self):
        return 4

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
class Rombo(Polígono):
    def __init__(self, lado, diagMayor, diagMenor):
        self.lado=lado
        self.diagMayor=diagMayor
        self.diagMenor=diagMenor

    def superficie(self):
        return (self.diagMenor*self.diagMayor)/2
    
    def perimetro(self):
        return self.lado*4

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
    
    @property
    def cantLados(self):
        return 4