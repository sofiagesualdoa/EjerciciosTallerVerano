# Girar 90 grados en sentido horario y luego frenar.

from controller import Robot
import math

TIME_STEP=32
MAX_VEL=6.28 
ROTACION=math.pi / 2

robot=Robot()
izq=robot.getDevice("wheel1 motor") 
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor") 
der.setPosition(float("inf"))
encoderIzq=izq.getPositionSensor()
encoderIzq.enable(TIME_STEP)

inicio=0

while robot.step(TIME_STEP) != -1:
    diferencia=abs(encoderIzq.getValue() - inicio)
    if diferencia < ROTACION:
        izq.setVelocity(MAX_VEL*0.5)
        der.setVelocity(-MAX_VEL*0.5)
    else:
        izq.setVelocity(0)
        der.setVelocity(0)
        break

# Martu: Está bien!! Fijate que no hace falta declarar los encoders de las dos ruedas si solo usás uno, y el robot
# no termina de hacer los 90°, TODO: ¿Existe algún sensor giroscopio o alguno similar que te permita mejorar el 
# comportamiento actual del código?.