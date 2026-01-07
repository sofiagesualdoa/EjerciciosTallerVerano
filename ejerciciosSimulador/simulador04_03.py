# Avanzar hasta encontrar una pared y frenar.

from controller import Robot

TIME_STEP=32
MAX_VEL=6.28

robot=Robot()
izq=robot.getDevice("wheel1 motor")
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor")
der.setPosition(float("inf"))
ps7 = robot.getDevice("ps7")
ps7.enable(TIME_STEP)
ps0 = robot.getDevice("ps0")
ps0.enable(TIME_STEP)

while robot.step(TIME_STEP) != -1:
    if ps7.getValue() < 0.05 or ps0.getValue() < 0.05:
        izq.setVelocity(0)
        der.setVelocity(0)
    else:
        izq.setVelocity(MAX_VEL)
        der.setVelocity(MAX_VEL)    

# Martu: Genial!!