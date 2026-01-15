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

z=0
x=0
def updateVars():
    global x,z
    x,_,z=gps.getValues()

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
    xInicial,zInicial=x,z
    while step()!=-1:
        dx=x-xInicial
        dz=z-zInicial
        distancia=math.sqrt(dx*dx + dz*dz)
        if distancia>=dist:
            break
        vel=MAX_VEL
        if dist/2<=distancia:
            vel=vel/2
        setVel(vel, vel)
    setVel(0, 0)

while step() != -1:
    avanzar(0.12)   
    delay(3000)
    # avanzar(1.2)  
    # delay(3000)
    break

# Martu: Fijate que en el simulador no termina frenando el robot... En el método updateVars se invoca a las variables 
# globales x, z pero ninguna está declarada por fuera del método. También, podrías en vez de usar una velocidad estándar
# para avanzar, ir regulándola con ayuda de una función lineal, que vaya disminuyendo la velocidad conforme el robot
# se vaya acercando a la distancia destino.

# corregido

# Martu: Bien!! Podrías incluso hacer una función que pasándole la distancia restante, defina cuál debe ser la velocidad 
# sabiendo que cuando la distancia restante es menor o igual a X debe ser cero o muy cercana a él, y al revés si la
# distancia es grande (no obligatorio).