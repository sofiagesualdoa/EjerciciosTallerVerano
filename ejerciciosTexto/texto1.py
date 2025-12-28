# Desarrollar un programa que saque las líneas en blanco repetidas 
# del archivo quijote.txt. Que cree un archivo quijoteej1.txt sin esas
# líneas en blanco repetidas.

with open("quijote.txt", "rt", encoding="utf-8") as texto1:
    with open("quijoteej1.txt", "wt", encoding="utf-8") as texto2:

        lineaBlanca = False

        for linea in texto1:
            if linea == "\n":
                if not lineaBlanca:
                    texto2.write(linea)
                    lineaBlanca=True
            else:
                texto2.write(linea)
                lineaBlanca=False