def invertir(cadena): 
    lista=cadena.split()
    cadena=""
    for elemento in lista:
        elemento = elemento[::-1]
        cadena+=f"{elemento} "
    return cadena
cadena="Esto es ejemplo"
print(f"Cadena invertida: {invertir(cadena)}")

# Martu: Bien!!