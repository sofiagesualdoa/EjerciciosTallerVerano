# Girar 180 grados en sentido antihorario y luego frenar.

from controller import Robot
import math

TIME_STEP=32
MAX_VEL=6.28 
ROTACION=math.pi

robot=Robot()
izq=robot.getDevice("wheel1 motor") 
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor") 
der.setPosition(float("inf"))
encoderDer=der.getPositionSensor()
encoderDer.enable(TIME_STEP)

inicio=0

while robot.step(TIME_STEP) != -1:
    diferencia=abs(encoderDer.getValue() - inicio)
    if diferencia < ROTACION:
        izq.setVelocity(-MAX_VEL*0.5)
        der.setVelocity(MAX_VEL*0.5)
    else:
        izq.setVelocity(0)
        der.setVelocity(0)
        break

# Martu: Muy bien!! Igual que en el otro ejercicio, el robot no termina de hacer los 180°, por lo que hay un TODO común :)