def Productos(lista, M):
    listaNueva=[]
    for prod in lista:
        if listaNueva==[]:
            listaNueva.append(prod)
        else:
            insertado = False
            for i in range(len(listaNueva)):
                if prod["pre"] > listaNueva[i]["pre"]:
                    listaNueva.insert(i, prod)
                    insertado = True
                    break
            if insertado == False:
                listaNueva.append(prod)
    return listaNueva[0:M]

lista=[{"prod":"pan", "pre": 100}, {"prod":"arroz", "pre": 50}, {"prod":"leche", "pre": 90}, {"prod":"carne", "pre": 300}]
M=2
print(Productos(lista, M))