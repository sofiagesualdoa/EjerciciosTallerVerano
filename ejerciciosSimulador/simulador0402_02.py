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

def evitarAgujero():
    print("Hay un agujero delante")
    setVel(0,0)
    delay(300)
    setVel(-MAX_VEL/6, -MAX_VEL/6)
    delay(800)
    setVel(0,0)
    girar(90)

while step()!=-1:
    b, g, r, a = colorSensor.getImage()
    print(izquierda.getValue(), derecha.getValue(), adelante.getValue())
    if r==41 and g==41 and b==41:
        evitarAgujero()
        continue
    elif r==209 and g==175 and b==101:
        print("Hay un Pantano, vamos más despacio")
        setVel(MAX_VEL/8, MAX_VEL/8)
        if  adelante.getValue() > 0.079:
            pass
        elif izquierda.getValue() > 0.079:
            girar(90)
        elif derecha.getValue() > 0.079:
            girar(-90)
        elif adelante.getValue() < 0.06:
            girar(90)
    elif r==231 and g==231 and b==231:
        print("Es baldosa normal")
        setVel(MAX_VEL/5, MAX_VEL/5)
        if  adelante.getValue() > 0.079:
            pass
        elif izquierda.getValue() > 0.079:
            girar(90)
        elif derecha.getValue() > 0.079:
            girar(-90)
        elif adelante.getValue() < 0.06:
            girar(90)
# falta terminar