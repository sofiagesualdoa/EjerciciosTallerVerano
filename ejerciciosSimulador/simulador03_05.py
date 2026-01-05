# Trazar un círculo con el movimiento del robot. 
# IMPORTANTE: Usar el mundo “mapa_circulito.wbt”

from controller import Robot

TIME_STEP=32
MAX_VEL=6.28

robot=Robot()
izq=robot.getDevice("wheel1 motor")
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor")
der.setPosition(float("inf"))

while robot.step(TIME_STEP) != -1:
    izq.setVelocity(MAX_VEL*0.8)
    der.setVelocity(MAX_VEL*0.5)