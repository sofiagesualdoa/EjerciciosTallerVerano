# Activar más de un sensor de distancia e imprimir 
# sus valores por consola.

from controller import Robot

TIME_STEP=32
robot=Robot()
sensor0=robot.getDevice("ps0") 
sensor0.enable(TIME_STEP) 
sensor1=robot.getDevice("ps1") 
sensor1.enable(TIME_STEP) 
sensor2=robot.getDevice("ps2") 
sensor2.enable(TIME_STEP) 
while robot.step(TIME_STEP) != -1:
    print(f"Distancia del sensor ps0: {sensor0.getValue()}")
    print(f"Distancia del sensor ps1: {sensor1.getValue()}")
    print(f"Distancia del sensor ps2: {sensor2.getValue()}")
    break

# Martu: Perfecto!! Aunque, el break no es necesario :)