#Algoritmo de Hoare
#Pivô: sempre elemento do meio do vetor 
#Algoritmo de Lomuto pode ocasionar em uma divisão do array discrepante em vetores decrescentes e crescentes 

def quicksort_original(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A) - 1
    if inicio < fim:
        #p recebe a posição correta do pivot
        p = partition(A, inicio, fim)
        #divisão e conquista
        quicksort_original(A, inicio, p-1)
        quicksort_original(A, p+1, fim)
    return A

def partition(A, inicio, fim):
    indice_pivot = (inicio + fim) // 2 
    valor_pivot = A[indice_pivot]
    i = inicio 
    j = fim 
    while i < j:
        while A[i] < valor_pivot:
            i = i + 1
        while A[j] > valor_pivot:
            j = j - 1  
        if i < j:
            A[j], A[i] = A[i], A[j]
    return j