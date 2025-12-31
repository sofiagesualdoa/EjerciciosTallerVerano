# Transformar una foto, de forma tal que la mitad superior quede 
# "virada" al rojo y la inferior al verde.

import cv2
img=cv2.imread("foto.jpg")
dimensiones=img.shape
mitad=int(dimensiones[0]/2)
img[:mitad][:,:,0]=0
img[:mitad][:,:,1]=0
img[mitad:][:,:,0]=0
img[mitad:][:,:,2]=0
cv2.imshow('Foto', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()