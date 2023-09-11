def lista_invertida(lista):
    i = len(lista)
    lista_aux = []

    while i > 0:
        lista_aux.append(lista[i - 1])

        i -= 1
    
    return lista_aux

lista = [1, 2, 3, 4, 5]
lista_aux = lista_invertida(lista)

print(lista_aux)
