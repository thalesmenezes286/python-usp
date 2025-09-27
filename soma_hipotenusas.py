def e_hipotenusa(i):
    """
    Verifica se um número inteiro i é o comprimento de uma hipotenusa
    de um triângulo retângulo com catetos inteiros.
    """
    i_quadrado = i * i
    for j in range(1, i):
        j_quadrado = j * j
        # Otimização: se j^2 já é maior que i^2, não faz sentido continuar.
        if j_quadrado > i_quadrado:
            break
        for k in range(j, i):
            k_quadrado = k * k
            if j_quadrado + k_quadrado == i_quadrado:
                return True
            # Otimização: se a soma de j^2 e k^2 já é maior que i^2,
            # os próximos k's (que são maiores) também serão.
            if j_quadrado + k_quadrado > i_quadrado:
                break

    return False


def soma_hipotenusas(n):
    """
    Calcula a soma de todas as hipotenusas inteiras entre 1 e n.
    """
    soma = 0
    for i in range(1, n + 1):
        if e_hipotenusa(i):
            soma += i

    return soma
