# Programar una función “avanzar” que reciba la distancia a recorrer y use el valor
# del GPS para calcular cuándo detenerse (tratar de que el movimiento sea lo más 
# preciso y rápido posible)

from controller import Robot
import math

def setVel(velIzq, velDer):
    izq.setVelocity(velIzq)
    der.setVelocity(velDer)

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()

izq=robot.getDevice("wheel2 motor")
izq.setPosition(float("inf"))
der=robot.getDevice("wheel1 motor")
der.setPosition(float("inf"))

gps=robot.getDevice("gps")
gps.enable(TIME_STEP)

def updateVars():
    global x,z
    x,_,z=gps.getValues()
    print(x,z)

def step():
    resu=robot.step(TIME_STEP)
    updateVars()
    return resu

def delay(ms):
    initTime = robot.getTime()
    while step() != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms:
            break

def avanzar(dist):
    xInicial, zInicial=x, z
    setVel(MAX_VEL/5, MAX_VEL/5)
    while step() != -1:
        dx=x-xInicial
        dz=z-zInicial
        distancia=math.sqrt(dx*dx + dz*dz)
        if distancia >= dist:
            break
    setVel(0, 0)

while step() != -1:
    avanzar(0.5)   
    delay(3000)
    avanzar(1.2)  
    delay(3000)
    break