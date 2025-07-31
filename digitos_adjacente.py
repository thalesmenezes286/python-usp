numero = int(input("Digite um número inteiro positivo: "))

anterior = numero % 10 
numero = numero // 10
numero_adjacente = False
cont = 0

while numero > 0 and not numero_adjacente:
    atual = numero % 10
    if atual == anterior:
        numero_adjacente = True
    else:
        cont = cont + 1
    anterior = atual
    numero = numero // 10

if numero_adjacente:
    print("Sim")
else:
    print("não")