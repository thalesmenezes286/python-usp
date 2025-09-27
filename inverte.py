# Crie uma lista vazia para guardar os números
numeros = []

# Inicie um laço para receber os números do usuário
while True:
    numero = int(input("Digite um número: "))
    
    # Se o número for 0, saia do laço
    if numero == 0:
        break
    
    # Adicione o número à lista
    numeros.append(numero)

# Imprima os números em ordem inversa
# A sintaxe [::-1] é uma forma simples de inverter uma lista em Python
print("Sequência invertida:")
for num in numeros[::-1]:
    print(num)