def Invertir(cadena): # Minúsculas...
    lista=cadena.split()
    cadena=""
    for elemento in lista:
        elemento = elemento[::-1]
        cadena+=f"{elemento} "
    return cadena
cadena="Esto es ejemplo"
print(f"Cadena invertida: {Invertir(cadena)}")

# Martu: Bien!!