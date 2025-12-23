def Contador(cadena):
    digitos=0
    for carac in cadena:
        if carac.isdigit():
            digitos+=1
    return digitos

cadena="Tengo  años"
print(f"Dígitos en la cadena: {Contador(cadena)}")

# Martu: Excelente :)