# Complexidade: O(N²) - Pior Caso

def bubblesort(vetor):
    comp = 0
    n = len(vetor)
    for i in range (n-1):
        for j in range (n-1):
            #contabilizando a quantidade de comparações efetuadas
            comp = comp + 1
            if vetor[j] > vetor[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
    return vetor, comp
