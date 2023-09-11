def soma_todos(lista):
    soma = 0

    for i in lista:
        soma += i
    
    return soma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = soma_todos(lista)

print("A soma de todos os numeros da lista é: ", soma)
