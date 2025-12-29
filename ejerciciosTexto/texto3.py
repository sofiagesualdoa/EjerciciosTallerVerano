# Hacer una función que dado el nombre de un archivo y una palabra, 
# devolver cuántas veces aparece la palabra en el archivo (como 
# palabra, no como cadena). contarPalabra(archivo, palabra).

def contarPalabra(archivo, palabra):
    cantPalabras=0
    with open(f"{archivo}.txt", "rt", encoding="utf-8") as texto:
        for linea in texto:
            palabras = linea.split()
            cantPalabras += palabras.count(palabra)
    return cantPalabras

palabra="la"
print(f"Cantidad de \"{palabra}\" en el quijote: {contarPalabra("prueba", palabra)}")

# Martu: Impecable!!