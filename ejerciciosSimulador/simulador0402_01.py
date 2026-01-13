# Identificar los distintos tipos de baldosa e imprimir en consola el nombre (NO los valores de RGB!)

from controller import Robot

TIME_STEP=32
robot=Robot()

colorSensor = robot.getDevice("colour_sensor")
colorSensor.enable(TIME_STEP)

def esPantano(r, g, b):
    return abs(r - 244) < 15 \
        and abs(g - 221) < 15 \
        and abs(b - 141) < 15

def esAgujero(r, g, b):
    return abs(r - 41) < 15 \
        and abs(g - 41) < 15 \
        and abs(b - 41) < 15

while robot.step(TIME_STEP) != -1:
    b, g, r, a = colorSensor.getImage()
    if esPantano(r, g, b):
        print(f"{robot.getTime():.2f}: Es Pantano")
    elif esAgujero(r, g, b):
         print(f"{robot.getTime():.2f}: Es un agujero")
    else:
        print(f"{robot.getTime():.2f}: Es baldosa normal")
       
# Martu: Bien!! Yo te recomiendo reemplazar los valores fijos de comparación por rangos relativos :p

# corregido