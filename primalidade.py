import math

# Recebe o número inteiro
numero = int(input("Digite um número inteiro positivo: "))

# 1. Números menores que 2 não são primos
if numero < 2:
    print("não primo")
# 2. O número 2 é primo
elif numero == 2:
    print("primo")    
# 3. Números pares maiores que 2 não são primos
elif numero % 2 == 0:
    print("não primo")
else: 
    i = 3
    limite = int(math.sqrt(numero))
    eh_primo = True

    while i <= limite:
        if numero % i == 0:
            eh_primo = False
            break
        i += 2

    if eh_primo:
        print("primo")
    else:
        print("não primo")
