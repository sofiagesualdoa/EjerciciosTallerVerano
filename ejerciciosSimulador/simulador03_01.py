# Prender ambos motores a la mitad de la velocidad máxima.

from controller import Robot

TIME_STEP=32
MAX_VEL=6.28 
robot=Robot()
izq=robot.getDevice("wheel1 motor") 
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor") 
der.setPosition(float("inf"))
while robot.step(TIME_STEP) != -1:
    izq.setVelocity(MAX_VEL*0.5)
    der.setVelocity(MAX_VEL*0.5)

# Martu: Cuidado porque la velocidad está mal escrita, debería ser MAX_VEL*0.5 (con punto en lugar de coma), ya que
# en Python el separador decimal es el punto, la "," se usa para separar elementos en listas, etc o listar argumentos 
# de una función.

# corregido