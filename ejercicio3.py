# lista=[5,7,9,"Hola",6,True,14.9,8]
# elemento=4
# index=elemento-1
# print(lista[index::])
# Martu: Está resuelto pero tratá de pensar cómo hacerlo sin usar slicing; es decir buscando el
# elemento dentro de la lista por contenido y no por índice. :)
# corregido: 
lista=[5,7,9,"Hola",6,True,14.9,8]
elemento=9
encontrado = False
listaNueva=[]
for objeto in lista:
    if objeto == elemento:
        encontrado = True
    if encontrado:
        listaNueva.append(objeto)
print(listaNueva)
# Martu: Puede ser que no me haya explicado bien, pero porbá usando el método index, y a partir de ahí sí usar slicing
# para poder imprimir el resto de la lista (perdón si no me expliqué bien antes :p)