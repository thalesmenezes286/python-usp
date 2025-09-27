# Exercício 2: Retângulo Sem Preenchimento (Vazado)
largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
    for j in range(largura):
        # Condições para imprimir '#' (borda)
        # Primeira linha (i == 0)
        # Última linha (i == altura - 1)
        # Primeira coluna (j == 0)
        # Última coluna (j == largura - 1)
        if i == 0 or i == altura - 1 or j == 0 or j == largura - 1:
            print("#", end="")
        else:
            print(" ", end="") # Imprime espaço para o interior
    print() # Adiciona uma quebra de linha