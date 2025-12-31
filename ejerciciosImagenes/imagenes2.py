# Transformar una foto, haciendo un espejo con la mitad izquierda 
# sobre la mitad derecha.

import cv2
img=cv2.imread("foto.jpg")
dimensiones=img.shape
mitad=int(dimensiones[1]/2)
img[:,mitad:]=img[:,0:mitad+1]
cv2.imshow('Foto', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()