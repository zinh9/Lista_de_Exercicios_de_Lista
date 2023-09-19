def ordenacao(lista):
    nova_lista = []

    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    for letra in alfabeto:
        for palavra in lista:
            if palavra[0] == letra:
                nova_lista.append(palavra)

    return nova_lista

lista = ["carlos", "alan", "bernado", "mariana", "enzo", "thais", "joao", "marcia", "renan"]
nova_lista = ordenacao(lista)

for i in nova_lista:
    print(i)
