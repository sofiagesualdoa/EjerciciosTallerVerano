# Hacer un función, que dada dos imágenes, copie la mitad superior de 
# la segunda imagen en la mitad superior de la primera y viceversa.

def cambiarImagenes(imagen1, imagen2):
    dimensiones=imagen1.shape
    mitadSuperior=int(dimensiones[0]/2)
    parte2=imagen2[0:mitadSuperior,:].copy()
    imagen2[0:mitadSuperior,:]=imagen1[0:mitadSuperior,:]
    imagen1[0:mitadSuperior,:]=parte2
    
import cv2
img1=cv2.imread("foto.jpg")
img2=cv2.imread("foto2.jpg")
if img1.shape != img2.shape:
       print("Las imágenes deben tener el mismo tamaño")
else:
    cambiarImagenes(img1, img2)
    cv2.imshow('Foto 1', img1)
    cv2.imshow('Foto 2', img2)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()