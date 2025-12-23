def arreglarCadena(cadNueva): 
    if cadNueva.endswith(".") == False:
        cadNueva += "."
    return cadNueva

cadena="hay pájaros y flores"
print(f"Cadena arreglada: {arreglarCadena(cadena)}")
print(cadena)

# Martu: Genial!
