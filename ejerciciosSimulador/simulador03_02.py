# Avanzar una distancia determinada y luego volver a la posición inicial.

from controller import Robot

TIME_STEP=32
MAX_VEL=6.28 
DISTANCIA=5

robot=Robot()
izq=robot.getDevice("wheel1 motor") 
izq.setPosition(float("inf"))
der=robot.getDevice("wheel2 motor") 
der.setPosition(float("inf"))
encoderIzq=izq.getPositionSensor()
encoderIzq.enable(TIME_STEP)

estado="avanzar"
inicio=0
while robot.step(TIME_STEP) != -1:
    posicion=encoderIzq.getValue()
    if estado == "avanzar":
        izq.setVelocity(MAX_VEL*0.5)
        der.setVelocity(MAX_VEL*0.5)
        if (posicion-inicio) >= DISTANCIA:
            estado = "retroceder"
            inicio = posicion
    elif estado == "retroceder":
        izq.setVelocity(-MAX_VEL*0.5)
        der.setVelocity(-MAX_VEL*0.5)
        if (inicio-posicion) >= DISTANCIA:
            estado="parar"
    else:
        izq.setVelocity(0)
        der.setVelocity(0)