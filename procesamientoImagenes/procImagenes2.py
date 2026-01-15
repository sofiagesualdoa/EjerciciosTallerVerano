# Ejercicio 2: hacer una función que dada una imagen, me devuelva el cartel recortado en thresh 
# (blanco y negro) o None si no es un cartel.

import math
import cv2
import numpy as np

contornos=()
thresh=None

def imagen(img):
    global contornos, thresh
    resultado=None
    gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh=cv2.threshold(gris, 140, 255, cv2.THRESH_BINARY)
    contornos, jerarquia = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos==():
        resultado=contornos
    return resultado

def recortar(img):
    resultado=None
    global contornos, thresh
    if len(contornos) == 1:
        approx=cv2.minAreaRect(contornos[0])
        x=int(approx[0][0])
        y=int(approx[0][1])
        mitadAncho=int(approx[1][0]/2)
        mitadAlto=int(approx[1][1]/2)
        rect=thresh[y-mitadAlto:y+mitadAlto, x-mitadAncho:x+mitadAncho] 
    return rect

img=cv2.imread("imagen1_1.png")
if not imagen(img)==None:
    rectangulo=recortar(img)
    if not rectangulo.all() == None:
        cv2.imshow("Cartel recortado", rectangulo)
        cv2.waitKey(0)
    else:
        print(None)
else:
    print(None)
