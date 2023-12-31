#Algoritmo de Lomuto
#Complexidade depende da escolha do pivot.
#O(N²) - Pior Caso. Escolha do pivot que divide o array em dois, um com 0 elementos e outro com n - 1 elementos.
#N*logN - Melhor Caso. Escolha do pivot que divide o array em dois, ambos com N/2 elementos.
#O melhor caso, no quicksort, é o predominante.
#Considerado o algortimo de ordenação mais rápido.
import random 

def quicksort_lomuto(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A) - 1
    if inicio < fim:
        #p recebe a posição correta do pivot
        p = randomized_partition(A, inicio, fim)
        #divisão e conquista
        quicksort_lomuto(A, inicio, p-1)
        quicksort_lomuto(A, p+1, fim)
    return A

def randomized_partition(A, p, r):
    #pivô é escolhido aleatoriamente entre p e r (exlcuindo r)
    aleatorio = random.randrange(p, r)
    #o último elemento recebeu um número aleatório do vetor, para não cair no pior caso em vetores decrescentes 
    A[aleatorio], A[r] = A[r], A[aleatorio]
    return partition(A, p, r)

def partition(A, inicio, fim):
    pivot = A[fim]
    #i separa os numeros menores que o pivot dos maiores
    #quando acha um menor, troca com o A[i] pois joga os menores pra esquerda, separando dos maiores
    #i aponta pro primeiro numero maior que o pivot
    i = inicio 
    for j in range (inicio, fim):
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i = i + 1
    A[i], A[fim] = A[fim], A[i]
    return i