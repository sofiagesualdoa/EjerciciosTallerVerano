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