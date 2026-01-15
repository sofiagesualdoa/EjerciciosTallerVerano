# hacer una función que dada una imagen me devuelva los contornos 
# si considera que es un cartel, o None si considera que no.

import math
import cv2
import numpy as np

def imagen(img):
    resultado=None
    gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh=cv2.threshold(gris, 140, 255, cv2.THRESH_BINARY)
    contornos, jerarquia = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contornos==():
        resultado=contornos
    return resultado

img=cv2.imread("imagen1_1.png")
print(imagen(img))
