import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 - 4 * a * c 

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"a raiz dupla desta equação é {raiz}")
else:
    raiz1 = (-b - math.sqrt(delta)) / (2*a)
    raiz2 = (-b + math.sqrt(delta)) / (2*a)

    menor = min(raiz1, raiz2)
    maior = max(raiz1, raiz2)
    print(f"as raízes da equação são {menor} e {maior}")