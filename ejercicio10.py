numero=15000
lista=list(str(numero))
contador=0
if lista[-1]!='0':
    print("No hay ceros al final")
else:
    reversed(lista)
    for elemento in lista:
        if elemento=='0':
            contador+=1
    print(f"Hay {contador} ceros")