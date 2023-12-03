# Complexidade: O(N²) - Pior Caso
# Número de operações: N*(N-1)/2

def insertion(vetor):
    comp = 0
    n = len(vetor)
    for i in range (1, n):
        j=i
        while j > 0:
            #numero de comparações
            comp = comp + 1
            if vetor[j] < vetor[j-1]:
                aux = vetor[j]
                vetor[j] = vetor[j-1]
                vetor[j-1] = aux
            
            j=j-1

    return vetor, comp
