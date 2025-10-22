import re

# Funções Auxiliares (fornecidas no esqueleto do exercício)
def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    
    # Os 6 traços linguísticos (assinatura) do texto de referência
    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    # Retorna a assinatura como uma lista de 6 elementos
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    # Sentenças são separadas por ".", "!" ou "?"
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas and sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    # Frases são separadas por ",", ":" ou ";"
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    # Palavras são separadas por espaços
    # O método .split() do Python já faz a separação por espaços e remove espaços extras
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = {}
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1 # Se a palavra já foi única e está se repetindo, decremente unicas
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1 # A primeira vez que a palavra aparece, ela é única
    return unicas # Razão Hapax Legomana

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    # Relação Type-Token
    freq = {}
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)

# --- Funções a serem implementadas (o cerne do algoritmo) ---

def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Fórmula do grau de similaridade (Sab): Soma dos módulos das diferenças dividida por 6
    # Sab = (1/6) * SOMA (|fi,a - fi,b|)
    
    soma_diferencas = 0
    # As assinaturas são listas com 6 elementos (os 6 traços linguísticos)
    for i in range(len(as_a)):
        # Calcula o valor absoluto da diferença para cada traço
        soma_diferencas += abs(as_a[i] - as_b[i])
        
    # Divide a soma por 6
    similaridade = soma_diferencas / 6
    return similaridade

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto (os 6 traços linguísticos).'''
    
    # 1. Obter sentenças, frases e palavras
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    
    for s in sentencas:
        frases_na_sentenca = separa_frases(s)
        frases.extend(frases_na_sentenca)
        for f in frases_na_sentenca:
            palavras_na_frase = separa_palavras(f)
            palavras.extend(palavras_na_frase)

    # 2. Totalizadores
    N_palavras = len(palavras)
    N_sentencas = len(sentencas)
    N_frases = len(frases)

    # Evita divisão por zero
    if N_palavras == 0 or N_sentencas == 0 or N_frases == 0:
        return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

    # 3. Cálculo dos 6 traços
    
    # 1. Tamanho médio de palavra (wal)
    soma_tamanhos_palavras = sum(len(p) for p in palavras)
    wal = soma_tamanhos_palavras / N_palavras
    
    # 2. Relação Type-Token (ttr)
    N_diferentes = n_palavras_diferentes(palavras)
    ttr = N_diferentes / N_palavras
    
    # 3. Razão Hapax Legomana (hlr)
    N_unicas = n_palavras_unicas(palavras)
    hlr = N_unicas / N_palavras
    
    # 4. Tamanho médio de sentença (sal)
    soma_tamanhos_sentencas = sum(len(s) for s in sentencas)
    sal = soma_tamanhos_sentencas / N_sentencas
    
    # 5. Complexidade de sentença (sac)
    sac = N_frases / N_sentencas
    
    # 6. Tamanho médio de frase (pal)
    soma_tamanhos_frases = sum(len(f) for f in frases)
    pal = soma_tamanhos_frases / N_frases
    
    # Retorna a assinatura completa
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    # O texto mais provável de estar infectado é aquele com a menor similaridade (o mais parecido)
    
    menor_similaridade = float('inf') # Inicializa com um valor muito alto
    texto_infectado = 0 # O índice do texto (começa em 1, por isso 0 é um valor inicial seguro)
    
    for i, texto in enumerate(textos):
        # 1. Calcula a assinatura do texto i
        assinatura_do_texto = calcula_assinatura(texto)
        
        # 2. Compara com a assinatura COH-PIAH
        similaridade = compara_assinatura(assinatura_do_texto, ass_cp)
        
        # 3. Verifica se esta é a menor similaridade encontrada
        if similaridade < menor_similaridade:
            menor_similaridade = similaridade
            # O número do texto é o índice + 1 (pois a contagem é 1, 2, 3...)
            texto_infectado = i + 1
            
    # Retorna o número do texto (1-based) que tem a menor similaridade
    return texto_infectado

# --- Bloco Principal de Execução ---

def main():
    # 1. Leitura da assinatura COH-PIAH
    assinatura_coh_piah = le_assinatura()
    
    # 2. Leitura dos textos a serem analisados
    textos_candidatos = le_textos()
    
    # 3. Avaliação e determinação do texto mais provável de ser plágio
    if textos_candidatos:
        texto_infectado_numero = avalia_textos(textos_candidatos, assinatura_coh_piah)
        print("\nO autor do texto", texto_infectado_numero, "está infectado com COH-PIAH")
    else:
        print("\nNenhum texto foi fornecido para análise.")

# Garante que a função main seja chamada quando o script for executado
if __name__ == '__main__':
    main()