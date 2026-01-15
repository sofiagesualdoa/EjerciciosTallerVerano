# Hacer un controlador que pueda explorar el mapa mapa_obstacles_1.wbt sin chocar con obstáculos.

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
lidar = robot.getDevice("lidar")
lidar.enable(TIME_STEP)
inu=robot.getDevice("inertial_unit")
inu.enable(TIME_STEP)
adelante=robot.getDevice("dsadelante")
adelante.enable(TIME_STEP)
izquierda=robot.getDevice("dsizquierda")
izquierda.enable(TIME_STEP)
derecha=robot.getDevice("dsderecha")
derecha.enable(TIME_STEP)

gradoRot=0
radianRot=0
def updateVars():
    global radianRot, gradoRot
    _, _, radianRot=inu.getRollPitchYaw()
    gradoRot=radianRot*180/math.pi

def step():
    resu=robot.step(TIME_STEP)
    updateVars()
    return resu

def delay(ms):
    initTime = robot.getTime()
    while step() != -1:
        if (robot.getTime() - initTime) * 1000.0 > ms:
            break

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

def hayObstaculo(capa):
    d = math.pi/16
    i0 = int((math.pi - d*4) / math.tau * 512)
    i1 = int((math.pi - d*1) / math.tau * 512)
    i2 = int((math.pi + d*0) / math.tau * 512)
    i3 = int((math.pi + d*1) / math.tau * 512)
    i4 = int((math.pi + d*4) / math.tau * 512)
    t_near = 0.06
    t_far = 0.2
    return (capa[i1] < t_near or capa[i2] < t_near or capa[i3] < t_near) \
        and (capa[i0] > t_far and capa[i4] > t_far)

while step()!=-1:
    print(f"izq: {izquierda.getValue()}, der: {derecha.getValue()}, ad: {adelante.getValue()}") 
    image = lidar.getRangeImage()
    capa1 = image[512:1024]   
    setVel(MAX_VEL/2, MAX_VEL/2)
    if izquierda.getValue() <= 0.02:
        girar(-5)
    elif derecha.getValue() <= 0.02:
        girar(5)
    if hayObstaculo(capa1):
        print("Hay Obstáculo!")
        setVel(-MAX_VEL/2, -MAX_VEL/2)
        delay(200)
        girar(-90)
        continue
    if izquierda.getValue() > 0.02 and adelante.getValue() > 0.02:
        setVel(MAX_VEL/2, MAX_VEL/2)
    elif izquierda.getValue() > 0.08:
        girar(90)
        setVel(MAX_VEL/3, MAX_VEL/2)
        delay(150)
    elif adelante.getValue() > 0.08:
        setVel(MAX_VEL/3, MAX_VEL/2)
    else:
        girar(-90)
    