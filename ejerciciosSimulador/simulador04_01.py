# Leer el valor de uno de los sensores de distancia e imprimirlo 
# por consola.

from controller import Robot

TIME_STEP=32
robot=Robot()
sensor=robot.getDevice("ps1") 
sensor.enable(TIME_STEP) 
while robot.step(TIME_STEP) != -1:
    print(f"Distancia del sensor ps: {sensor.getValue()}")

# Martu: Perfecto!!