numero = int(input("Digite o valor de n: "))

if numero < 0:
    print("0")
elif numero == 0 or numero == 1:
    print("1")
else:   

    fatorial = 1

    for i in range(1, numero + 1):
        fatorial = fatorial * i
    
    print(str(fatorial))
