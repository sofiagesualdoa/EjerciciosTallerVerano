# Hacer lo mismo que en el ejercicio 2 con el video.

import cv2
import numpy as np
cam=cv2.VideoCapture(0)
while(True):
    ret, cuadro=cam.read()
    if ret:
        dimension=cuadro.shape
        mitad=int(dimension[1]/2)
        cuadro[:,mitad:]=cuadro[:,0:mitad]
        cv2.imshow("Cámara", cuadro)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

# Martu: Impecable!