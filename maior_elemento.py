#Verifica qual o maior elemento de uma lista
def maior_elemento(lista):
    maior = lista[0]   # começa assumindo que o primeiro é o maior
    for numero in lista:
        if numero > maior:
            maior = numero

    return maior 