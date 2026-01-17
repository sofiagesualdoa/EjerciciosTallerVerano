# Ejercicio 4: realizar una función que dada la imagen de la cámara, me devuelva None si no es un cartel, 
# o el cartel ya rotado y limpio de contexto.

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

def buscarContornosThresh(img):
    global contornos
    contornos, jerarquia = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

x=0
y=0
mitadAlto=0
mitadAncho=0
angulo=0

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

img=cv2.imread("imagen1_5.png")
if not imagen(img)==None:
    alto, ancho=thresh.shape[0], thresh.shape[1]
    M=cv2.getRotationMatrix2D((ancho/2,alto/2),angulo,1) 
    thresh_rot=cv2.warpAffine(thresh,M,(ancho,alto))   
    imagen_rot=cv2.warpAffine(img,M,(ancho,alto))
    buscarContornosThresh(thresh_rot)
    rectangulo=recortar(imagen_rot)
    if rectangulo.all() != None:
        cv2.imshow("Cartel recortado", rectangulo)
        cv2.waitKey(0)
    else:
        print(None)
else:
    print(None)
