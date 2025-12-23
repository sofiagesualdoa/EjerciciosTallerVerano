def ArreglarCadena(cadNueva): # Recordar que las funciones deben tener nombres que NO inicien con mayúscula
    cadNueva = cadNueva.capitalize()
    if cadNueva.endswith(".") == False:
        cadNueva += "."
    return cadNueva

cadena="hay pájaros y flores"
print(f"Cadena arreglada: {ArreglarCadena(cadena)}")
print(cadena)

# Martu: Genial!