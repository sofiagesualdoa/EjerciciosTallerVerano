# Girar hasta detectar el hueco alrededor del robot

from controller import Robot

TIME_STEP=32
MAX_VEL=6.28

robot=Robot()
izq=robot.getDevice("wheel1 motor")
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor")
der.setPosition(float("inf"))
ps6 = robot.getDevice("ps6")
ps6.enable(TIME_STEP)


while robot.step(TIME_STEP) != -1:
    if ps6.getValue()>0.12:
        izq.setVelocity(0)
        der.setVelocity(0)
    else:
        izq.setVelocity(MAX_VEL*0.5)
        der.setVelocity(-MAX_VEL*0.5)

# Martu: Muy bien!! :)