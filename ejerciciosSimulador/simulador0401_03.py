# Usar las nuevas funciones de movimiento para desarrollar un algoritmo de navegación avanza 0.12 
# si (nada a la izquierda) giro 90 sino si (nada enfrente) pass sino si (nada derecha) giro -90


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
inu=robot.getDevice("inertial_unit")
inu.enable(TIME_STEP)
derecha=robot.getDevice("dsderecha")
derecha.enable(TIME_STEP)
izquierda=robot.getDevice("dsizquierda")
izquierda.enable(TIME_STEP)
adelante=robot.getDevice("dsadelante")
adelante.enable(TIME_STEP)

gradoRot=0
radianRot=0

def updateVars():
    global x,z,radianRot, gradoRot
    _, _, radianRot=inu.getRollPitchYaw()
    gradoRot=radianRot*180/math.pi
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
    xInicial, zInicial=x, z
    setVel(MAX_VEL/5, MAX_VEL/5)
    while step() != -1:
        dx=x-xInicial
        dz=z-zInicial
        distancia=math.sqrt(dx*dx + dz*dz)
        if distancia >= dist:
            break
    setVel(0, 0)

def corregirAngulo(angulo):
    if angulo > 180:
        angulo-=360
    else:
        if angulo < -180:
            angulo += 360
    return angulo

def girar(cuantoRotar):
    anguloInicial=gradoRot
    anguloDestino=corregirAngulo(anguloInicial+cuantoRotar)
    sentido=1 
    if cuantoRotar < 0:
        sentido=-1
    while step() != -1:
        anguloActual=gradoRot
        diferencia=corregirAngulo(anguloDestino-anguloActual)
        if abs(diferencia) < 2:
            break
        setVel(-MAX_VEL/5*sentido, MAX_VEL/5*sentido)
    setVel(0, 0)

while step() != -1:
    avanzar(0.12)
    if izquierda.getValue() > 0.08:
        girar(90)
    elif  adelante.getValue() > 0.08:
        pass
    elif derecha.getValue() > 0.08:
        girar(-90)

# Martu: Probé el código en el mapa "mapa_noholes_1" (ahí lo subo) llega un momento dado de la simulación en donde el
# robot se termina chocando con una pared, creo que podría ser el error de las variables globales que se viene arrastrando
# hace un par de ejercicios.