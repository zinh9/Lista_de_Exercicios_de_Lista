def lista_usuario():
    lista = []
    resposta = "sim"
    
    while resposta == "sim":
        lista.append(input("Digite qual palavra deseja adicionar na lista: "))
        resposta = input("Deseja adicionar mais palavras: ")

    return lista

def palavra_maior(lista):
    print("Palavras com caracteres maior ou igual a 5: \n")
    
    for palavra in lista:
        if len(palavra) >= 5:
            print(palavra)

lista = lista_usuario()
palavra_maior(lista)
