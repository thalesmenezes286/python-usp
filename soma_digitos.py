numero = int(input("Digite um número inteiro: "))

soma = 0
while numero > 0:
    digito = numero % 10   # pega o último dígito
    soma += digito         # soma o dígito
    numero //= 10          # remove o último dígito

print(soma)