def maior(lista):
    maior_num = lista[0]
    
    for i in lista:
        if i > maior_num:
            maior_num = i
    
    print(maior_num)

lista = [4, 5, 8, 7, 2, 1, 0, 7, 9]
maior(lista)
