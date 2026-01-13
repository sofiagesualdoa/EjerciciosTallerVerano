# Exportar en archivo csv sólo la capa 1 de la nube de puntos

from controller import Robot
import numpy as np
import csv

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()
lidar = robot.getDevice("lidar")
lidar.enable(TIME_STEP)
lidar.enablePointCloud()

FOLDER = r"C:\Users\sofig\Documents\point_cloud.csv"
points=[]

while robot.step(TIME_STEP) != -1:
    points = lidar.getPointCloud()[512:1024]
    points = [(p.x, p.y, p.z, p.layer, p.time) for p in points]
    break
    
with open(FOLDER, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(("x", "y", "z", "layer", "time"))
        writer.writerows(points)