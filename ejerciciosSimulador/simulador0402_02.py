# Hacer un robot que recorra el mapa easy1.wbt y NO se caiga en agujeros.

from controller import Robot
import math

def setVel(velIzq, velDer):
    izq.setVelocity(velIzq)
    der.setVelocity(velDer)

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()
colorSensor = robot.getDevice("colour_sensor")
colorSensor.enable(TIME_STEP)
izq=robot.getDevice("wheel2 motor")
izq.setPosition(float("inf"))
der=robot.getDevice("wheel1 motor")
der.setPosition(float("inf"))
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

agujero=False

while step()!=-1: 
    b,g,r,a = colorSensor.getImage()
    print(f"izq: {izquierda.getValue()}, der: {derecha.getValue()}, ad: {adelante.getValue()}")
    if r==41 and g==41 and b==41:
        print("Agujero detectado")
        agujero=True
        setVel(-MAX_VEL/5, -MAX_VEL/5)
        delay(1000)
        setVel(0,0)
        girar(90)
        continue
    if agujero==True:
        girar(90)  
        while adelante.getValue() < 0.08:
            girar(90)
        setVel(MAX_VEL/6, MAX_VEL/6)
        delay(4000)
        agujero=False 
    if r==209 and g==175 and b==101:
        velocidad=MAX_VEL/6
    else:
        velocidad=MAX_VEL/4
    if izquierda.getValue() < 0.1 and adelante.getValue() > 0.07:
        setVel(velocidad, velocidad)
    elif izquierda.getValue() < 0.1 and adelante.getValue() < 0.08 and derecha.getValue() >= 0.8:
        girar(-90)
    elif adelante.getValue() < 0.08:
        girar(90)
    else:
        girar(90)

# Martu: Está bien! Te aconsejo que de alguna manera puedas "almacenar" qué lugares del mapa recorriste y cuáles no, 
# lo que te ayudaría a poder terminar de recorrer el mapa completo :).