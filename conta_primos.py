def eh_primo(num):
    if num < 2:
        return False
    divisor = 2
    while divisor * divisor <= num:  # só precisa ir até a raiz quadrada
        if num % divisor == 0:
            return False
        divisor += 1
    return True

def n_primos(n):
    contador = 0
    numero = 2
    while numero <= n:
        if eh_primo(numero):
            contador += 1
        numero += 1

    return contador

print(n_primos(2))   
print(n_primos(4))    
print(n_primos(121))  