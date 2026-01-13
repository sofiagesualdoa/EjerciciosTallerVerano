# Extraer y visualizar sólo la capa 1 de la imagen de profundidad

from controller import Robot
import numpy as np
import cv2

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()
lidar = robot.getDevice("lidar")
lidar.enable(TIME_STEP)

def partition(seq, length):
    chunks = []
    chunk = []
    for e in seq:
        chunk.append(e)
        if len(chunk) == length:
            chunks.append(chunk)
            chunk = []
    if len(chunk) > 0:
        chunks.append(chunk)
    return chunks

def flatten(t):
    return [item for sublist in t for item in sublist]

while robot.step(TIME_STEP) != -1:
    capa1 = lidar.getRangeImage()[512:1024]
    pixels = []
    for d in flatten([p*32 for p in partition(capa1, 512)]):
        color = d * 255
        color = int(max(min(color, 255), 0))
        pixels.append(color)
    img = np.frombuffer(bytes(pixels), np.uint8).reshape((1*32, 512))
    cv2.imshow("LiDAR Capa 1", img)
    cv2.waitKey(1)