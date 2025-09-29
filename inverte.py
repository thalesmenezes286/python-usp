numeros = []  # lista para armazenar os números

while True:
    n = int(input("Digite um número: "))
    if n == 0:  # se for zero, encerra
        break
    numeros.append(n)  # adiciona à lista

# imprime a lista invertida
for numero in reversed(numeros):
    print(numero)
