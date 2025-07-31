#Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro 
# e devolve o maior número primo menor ou igual ao número passado à função

import math

def eh_primo(num):

    if(num < 2):
        primo = False
    else:
        #Assume que o número é primo 
        primo = True

        for i in range(2, int(math.sqrt(num)) + 1):

            if num % i == 0:
                primo = False
                break

        # Exibe o resultado
        if primo:
            return True
        else:
            return False

def maior_primo(num):

    while num > 1:

        if eh_primo(num):
            return num
        
        num = num -1

    return None


num = int(input("Digite um número inteiro positivo: "))
print(f"O maior número primo entre { num } até 1 é: ",maior_primo(num))