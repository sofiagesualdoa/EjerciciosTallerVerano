# Programar una función “girar” que reciba el ángulo a girar y use el 
# valor del inertial unit para decidir cuándo detenerse (tratar de que 
# el movimiento sea lo más preciso y rápido posible)


from controller import Robot
import math

TIME_STEP=32
MAX_VEL=6.28 
robot=Robot()
izq=robot.getDevice("wheel2 motor") 
izq.setPosition(float("inf"))
der=robot.getDevice("wheel1 motor") 
der.setPosition(float("inf"))
inu=robot.getDevice("inertial_unit")
inu.enable(TIME_STEP)

radianRot=0
gradoRot=0
def updateVars():
    global radianRot, gradoRot
    _, _, radianRot=inu.getRollPitchYaw()
    gradoRot=radianRot*180/math.pi

def step():
    resultado=robot.step(TIME_STEP)
    updateVars()
    return resultado

def delay(ms):
    inicio=robot.getTime()
    while step() != -1:
        if(robot.getTime() - inicio)*1000.0 > ms:
            break

def setVel(velIzq, velDer):
    izq.setVelocity(velIzq)
    der.setVelocity(velDer)

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
    girar(180)
    # delay(5000)
    # girar(40)
    # delay(5000)
    break

# Martu: Genial!!

