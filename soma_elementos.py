def soma_elementos(lista):
    total = 0
    for numero in lista:
        if isinstance(numero, int):
            total += numero

    return total

lista = [1,1,1,2]
print(soma_elementos(lista))