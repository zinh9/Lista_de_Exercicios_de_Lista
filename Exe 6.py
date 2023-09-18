def num_removido(lista):
    i = 1
    j = 1

    for n in lista:
        while i < len(lista):
            if n == lista[i]:
                lista.remove(lista[i])
            
            i += 1

        j += 1
        i = j
    
    return lista

lista = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 9]
nova_lista = num_removido(lista)

for i in nova_lista:
    print(i)
