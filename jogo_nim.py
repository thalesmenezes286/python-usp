# Módulo que implementa o jogo do NIM
def computador_escolhe_jogada(n, m):
    """
    Função que implementa a estratégia vencedora do computador.
    
    Args:
        n (int): Número de peças no tabuleiro.
        m (int): Número máximo de peças a serem removidas em uma jogada.

    Returns:
        int: Número de peças que o computador deve remover.
    """
    if n <= m:
        return n
    
    if n % (m + 1) == 0:
        return m
    else:
        return n % (m + 1)


def usuario_escolhe_jogada(n, m):
    """
    Função que solicita a jogada do usuário e a valida.

    Args:
        n (int): Número de peças no tabuleiro.
        m (int): Número máximo de peças a serem removidas em uma jogada.

    Returns:
        int: Número de peças que o usuário escolheu remover.
    """
    while True:
        try:
            jogada = int(input("Quantas peças você vai tirar? "))
            if 1 <= jogada <= m and jogada <= n:
                return jogada
            else:
                print("\nOops! Jogada inválida! Tente de novo.\n")
        except ValueError:
            print("\nOops! Jogada inválida! Tente de novo.\n")


def partida():
    """
    Função que gerencia uma partida completa do jogo do NIM.
    """
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("\nVocê começa!\n")
        vez_do_computador = False
    else:
        print("\nComputador começa!\n")
        vez_do_computador = True

    while n > 0:
        if vez_do_computador:
            jogada = computador_escolhe_jogada(n, m)
            n -= jogada
            print(f"O computador tirou {jogada} peças.")
            vez_do_computador = False
            if n > 0:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            else:
                print("Fim do jogo! O computador ganhou!")
                return "computador"
        else:
            jogada = usuario_escolhe_jogada(n, m)
            n -= jogada
            print(f"\nVocê tirou {jogada} peças.")
            vez_do_computador = True
            if n > 0:
                print(f"Agora restam {n} peças no tabuleiro.\n")
            else:
                print("Fim do jogo! Você ganhou!")
                return "usuario"


def campeonato():
    """
    Função que gerencia um campeonato de três partidas do jogo do NIM.
    """
    placar_usuario = 0
    placar_computador = 0

    for i in range(1, 4):
        print(f"\n**** Rodada {i} ****\n")
        vencedor = partida()
        if vencedor == "usuario":
            placar_usuario += 1
        else:
            placar_computador += 1
    
    print("\n**** Final do campeonato! ****\n")
    print(f"Placar: Você {placar_usuario} X {placar_computador} Computador")


def main():
    """
    Função principal que inicia o jogo.
    """
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    while True:
        try:
            escolha = int(input())
            if escolha == 1:
                print("\nVocê escolheu uma partida isolada!\n")
                partida()
                break
            elif escolha == 2:
                print("\nVocê escolheu um campeonato!\n")
                campeonato()
                break
            else:
                print("Escolha inválida. Por favor, digite 1 ou 2.")
        except ValueError:
            print("Escolha inválida. Por favor, digite 1 ou 2.")

if __name__ == "__main__":
    main()