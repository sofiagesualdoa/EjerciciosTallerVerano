# Hacer un controlador que detecte obstáculos usando sensores de distancia

from controller import Robot
import math

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()
lidar = robot.getDevice("lidar")
lidar.enable(TIME_STEP)

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

while robot.step(TIME_STEP) != -1:
    image = lidar.getRangeImage()
    capa1 = image[512:1024]
    if hayObstaculo(capa1):
        print("Hay Obstáculo!")
    else:
        print("No hay Obstáculo")