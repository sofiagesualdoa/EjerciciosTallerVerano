# Exportar en archivo csv sólo la capa 1 de la nube de puntos

from controller import Robot
import numpy as np
import csv
import os

TIME_STEP=32
MAX_VEL=6.28
robot=Robot()
lidar = robot.getDevice("lidar")
lidar.enable(TIME_STEP)
lidar.enablePointCloud()

FOLDER = r"C:\Users\sofig\Documents"
points=[]

def csvExiste(nombre):
    global FOLDER
    if not os.path.exists(FOLDER+f"{nombre}"):
        with open(FOLDER+f"{nombre}", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(("x", "y", "z", "layer", "time"))
            writer.writerows(points)

while robot.step(TIME_STEP) != -1:
    points = lidar.getPointCloud()[512:1024]
    points = [(p.x, p.y, p.z, p.layer, p.time) for p in points]
    break
    
nombre=r"\nubePuntosCapa1.csv"
csvExiste(nombre)

with open(FOLDER + f"{nombre}", "r", newline="") as f:
        reader = csv.reader(f)
        

# Martu: Funciona únicamente cuando el archivo csv ya existe previamente, podrías agregar una función que dado un nombre
# para el csv, cree el archivo si no existe.

# corregido