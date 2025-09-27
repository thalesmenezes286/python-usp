largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

linha = 0
while linha < altura:
    coluna = 0
    while coluna < largura:
        if linha == 0 or linha == altura - 1 or coluna == 0 or coluna == largura - 1:
            print("#", end="")
        else:
            print(" ", end="")
        coluna += 1
    print()
    linha += 1
