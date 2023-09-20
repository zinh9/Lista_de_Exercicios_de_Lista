def substituir(lista):
    i = 0
    
    while i < len(lista):
        if lista[i] % 2 == 0:
            lista[i] = 0
        
        i += 1
    
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nova_lista = substituir(lista)

print(nova_lista)
