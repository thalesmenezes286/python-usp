def fatorial(numero):

    if numero < 0:
        return 0
    elif numero == 0 or numero == 1:
        return 1
    else:   
        
        fatorial = 1

        for i in range(1, numero + 1):
            fatorial = fatorial * i
        return fatorial
    
def numero_binomial(n, k):
    
    return fatorial(n) // (fatorial(k) * fatorial(n-k))

#numero = int(input("Digite um número inteiro positivo: "))
print(numero_binomial(5,3))