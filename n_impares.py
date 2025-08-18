# Solicita ao usuário para digitar o valor de n
n = int(input("Digite o valor de n: "))

# Garante que n é positivo, caso o usuário digite um valor inválido
if n <= 0:
    print("O valor de n deve ser um número inteiro positivo.")
else:
    # A variável 'contador' vai nos ajudar a contar quantos números ímpares já imprimimos
    contador = 0
    # A variável 'numero_impar' começa com 1, o primeiro número ímpar
    numero_impar = 1
    
    # O loop 'while' continua enquanto o contador for menor que n
    while contador < n:
        # Imprime o número ímpar atual
        print(numero_impar)
        # Incrementa o número ímpar para o próximo (por exemplo, de 1 para 3, de 3 para 5)
        numero_impar += 2
        # Aumenta o contador para sabermos que já imprimimos mais um número
        contador += 1