
#Escreva a função vogal que recebe um único caractere como parâmetro e 
# devolve True se ele for uma vogal e False se for uma consoante.
def vogal(caracter):
    vogais = ['a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    letra = str(caracter)  # converte para string e minúscula

    if len(letra) == 1 and letra.isalpha():
        if letra in vogais:
            return True
        else:
            return False
    else:
        return False  # caso não seja uma única letra
    

digito = input("Digite uma letra:")

while digito != "0":

    if digito == "0":
        break

    if vogal(digito):
        print(f" {digito} é uma vogal")
        break
    else:
        print(f" {digito} é uma consoante")
        break
 