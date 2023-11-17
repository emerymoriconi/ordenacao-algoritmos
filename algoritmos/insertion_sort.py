# Complexidade: O(N²) - Pior Caso
# Número de operações: N*(N-1)/2

def insertion(vetor):
    n = len(vetor)
    for i in range (1, n):
        j=i
        while j > 0:
            if vetor[j] < vetor[j-1]:
                aux = vetor[j]
                vetor[j] = vetor[j-1]
                vetor[j-1] = aux
            
            j=j-1

    return vetor
