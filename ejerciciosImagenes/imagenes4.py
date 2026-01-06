# Invertir los cuadrantes: que el superior izquierdo pase al inferior 
# derecho, y el superior derecho al inferior izquierdo. Y el superior 
# derecho al inferior izquierdo y viceversa. 

import cv2
img=cv2.imread("foto.jpg")
imagenNueva=cv2.imread("foto.jpg") # Martu: Podrías hacer una copia con img.copy()
dimensiones=img.shape
mitadSuperior=int(dimensiones[0]/2)
mitadIzquierda=int(dimensiones[1]/2)
derechoInferior=img[mitadSuperior+1:,mitadIzquierda:]
superiorIzquierdo=img[0:mitadSuperior,0:mitadIzquierda+1]
izquierdoInferior=img[mitadSuperior+1:,0:mitadIzquierda]
derechoSuperior=img[0:mitadSuperior,mitadIzquierda+1:]
imagenNueva[mitadSuperior+1:,mitadIzquierda:]=superiorIzquierdo
imagenNueva[0:mitadSuperior,0:mitadIzquierda+1]=derechoInferior
imagenNueva[mitadSuperior+1:,0:mitadIzquierda]=derechoSuperior
imagenNueva[0:mitadSuperior,mitadIzquierda+1:]=izquierdoInferior
cv2.imshow('Foto', imagenNueva)
cv2.waitKey(0) 
cv2.destroyAllWindows()

# Martu: Excelente!