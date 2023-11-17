A = [4, 5, 1, 9, 0, 8, 6, 3, 2, 7]

def bubblesort(vetor):
    n = len(vetor)
    for i in range (n-1):
        for j in range (n-1):
            if vetor[j] > vetor[j+1]:
                aux = vetor[j]
                vetor[j] = vetor[j+1]
                vetor[j+1] = aux
    return vetor

print(bubblesort(A))