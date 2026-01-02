# Imaginen la imagen dividida en 4 partes. Repetir el cuadrante superior 
# izquierdo en el inferior derecho, y el superior derecho en el inferior
# izquierdo.

import cv2
img=cv2.imread("foto.jpg")
dimensiones=img.shape
mitadSuperior=int(dimensiones[0]/2)
mitadIzquierda=int(dimensiones[1]/2)
img[mitadSuperior+1:,mitadIzquierda:]=img[0:mitadSuperior,0:mitadIzquierda+1]
img[mitadSuperior+1:,0:mitadIzquierda]=img[0:mitadSuperior,mitadIzquierda+1:]
cv2.imshow('Foto', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()