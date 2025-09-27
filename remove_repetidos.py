#Remove números inteiros de uma lista e devolve a lista de forma ordenada
def remove_repetidos(lista):
    nova_lista = []
    for numero in lista:
        if isinstance(numero, int) and numero not in nova_lista:
            nova_lista.append(numero)
            lista_ordenada = sorted(set(nova_lista))

    return lista_ordenada    

