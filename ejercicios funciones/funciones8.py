def Coincidencia(c1, c2):
    resultado=None
    primeraVez=c1.find(c2)
    segundaVez=c1.find(c2,primeraVez+1)
    if segundaVez!=-1:
        resultado=segundaVez
    return resultado

cadena1="Esto es una estatua"
cadena2="st"
print(Coincidencia(cadena1,cadena2))