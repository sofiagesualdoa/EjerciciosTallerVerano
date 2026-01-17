# Ejercicio 3: armar una función que dada una imagen me devuelva la letra si es un cartel, o None si no lo es.

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

x=0
y=0
mitadAlto=0
mitadAncho=0

def recortar(img):
    rect=None
    global contornos, thresh, x, y, mitadAlto, mitadAncho, angulo
    if len(contornos) == 1:
        approx=cv2.minAreaRect(contornos[0])
        x=int(approx[0][0])
        y=int(approx[0][1])
        mitadAncho=int(approx[1][0]/2)
        mitadAlto=int(approx[1][1]/2)
        angulo=approx[2]
        rect=img[y-mitadAlto:y+mitadAlto, x-mitadAncho:x+mitadAncho] 
    return rect

img=cv2.imread("imagen1_3.png")
if not imagen(img)==None:
    rectangulo=recortar(thresh)
    if not rectangulo == None:
        cuadritoArriba=thresh[y-mitadAlto:y-int(mitadAlto/3), x-int(mitadAncho/3):x+int(mitadAncho/3)]
        cuadritoAbajo=thresh[y+int(mitadAlto/3):y+mitadAlto, x-int(mitadAncho/3):x+int(mitadAncho/3)]
        pixelesNegrosAbajo=np.count_nonzero(cuadritoAbajo==0)
        pixelesNegrosArriba=np.count_nonzero(cuadritoArriba==0)
        if pixelesNegrosAbajo==0 and pixelesNegrosArriba==0:
            print("Es una H")
        elif pixelesNegrosArriba==0 and pixelesNegrosAbajo!=0:
            print("Es una U")
        elif pixelesNegrosAbajo!=0 and pixelesNegrosArriba!=0:
            print("Es una S")
    else:
        print(None)
else:
    print(None)
