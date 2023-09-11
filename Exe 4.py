def lista_compras():
    lista = []

    while True:
        item = input("Digite a compra que deseja adicionar na lista (digite 'parar' para encerrar): ")
        
        if item == "parar":
            break
        
        lista.append(item)
    
    return lista

lista = lista_compras()

print("A sua lista de compras tem os itens: \n")
for i in lista:
    print(i)
