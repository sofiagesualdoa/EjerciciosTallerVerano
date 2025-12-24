# Crear la clase RobotLucha, con el atributo fuerza (valor entre 1 y 10), y vivo 
# (valor True o False, arranca en True). Crear el constructor que recibe la fuerza. 
# Crear un método agregarFuerza(valor), que aumenta la fuerza en ese valor, no superando 10. 
# Crear el método de instancia luchar(otroRobot), que recibe otro robot y devuelve True o False 
# si ganó el robot que recibió el método, y disminuye su fuerza en el valor de fuerza que tenía 
# el otro robot. El robot que pierde pasa su atributo vivo a False.

# r1=RobotLucha(8)

# r2=RobotLucha(6)

# print(r1.fuerza) #8

# print(r2.fuerza) #6

# print(r1.luchar(r2)) #True

# print(r1.fuerza) #2

# print(r2.vivo) #False

class RobotLucha:
    def __init__(self, fuerza):
        self.fuerza=fuerza
        self.vivo=True
    
    def agregarFuerza(self, valor):
        if(self.fuerza + valor) > 10:
            self.fuerza=10
        else:
            self.fuerza+=valor
    
    def luchar(self, otroRobot):
        gano=True
        fuerza=self.fuerza
        self.fuerza-=otroRobot.fuerza
        otroRobot.fuerza-=fuerza
        if self.fuerza<=0:
            self.vivo=False
            gano=False
        elif otroRobot.fuerza<=0:
            otroRobot.vivo=False
        return gano

r1=RobotLucha(8)
r2=RobotLucha(6)
print(r1.fuerza) 
print(r2.fuerza)
print(r1.luchar(r2))
print(r1.fuerza)
print(r2.vivo)