lista=[7,True,"list",15,"números"]
if(len(lista) >= 2):
    elemento=lista[0]
    del lista[0]
    lista.append(elemento)
    print(f"La lista modificada es: {lista}")
else:
    print(f"La lista queda igual: {lista}")