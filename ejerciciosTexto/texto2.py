# Desarrollar un programa que escriba cada línea de 
# quijote.txt invertida.

with open("quijote.txt", "rt", encoding="utf-8") as texto1:
    with open("quijoteInvertido.txt", "wt", encoding="utf-8") as texto2:
        for linea in texto1:
            lineanueva=linea[::-1]
            texto2.write(lineanueva)

# Martu: Perfecto!!