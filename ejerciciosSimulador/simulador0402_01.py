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

while robot.step(TIME_STEP) != -1:
    b, g, r, a = colorSensor.getImage()
    # if esPantano(r, g, b):
    #     print(f"{robot.getTime():.2f}: Es Pantano")
    # else:
    #     print("Es baldosa normal")
    # print(f"R:{r} G:{g} B:{b}")
    if r==231 and g==231 and b==231:
        print("Es baldosa normal")
    elif r==209 and g==175 and b==101:
        print("Es pantano")
    elif r==41 and g==41 and b==41:
        print("Es un agujero")