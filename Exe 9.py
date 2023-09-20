def comum(lista_1, lista_2):
    comum = []

    for n in lista_1:
        if n in lista_2:
            comum.append(n)

    return comum

lista_1 = [10, True, "enzo", 3.7, "gay", False, 100]
lista_2 = [1, False, "mari", 3.7, "gay", True, 99]
elementos_comum = comum(lista_1, lista_2)

print(elementos_comum)
