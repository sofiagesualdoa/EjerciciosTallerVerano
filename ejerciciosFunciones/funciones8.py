def coincidencia(c1, c2): 
    resultado=None
    primeraVez=c1.find(c2)
    segundaVez=c1.find(c2,primeraVez+1)
    if segundaVez!=-1:
        resultado=segundaVez
    return resultado

cadena1="Esto es una estatua"
cadena2="una"
print(coincidencia(cadena1,cadena2))

# Martu: Excelente :D
