def ArreglarCadena(cadNueva):
    cadNueva = cadNueva.capitalize()
    if cadNueva.endswith(".") == False:
        cadNueva += "."
    return cadNueva

cadena="hay pájaros y flores"
print(f"Cadena arreglada: {ArreglarCadena(cadena)}")
print(cadena)