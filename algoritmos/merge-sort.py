# Complexidade: O(N*logN) - Pior Caso

A = [4, 5, 1, 9, 0, 8, 6, 3, 2, 7]

def mergesort(A, inicio=0, fim=None):
    if fim is None:
        fim = len(A)
    if (fim - inicio > 1):
        # "//" divisão inteira 
        meio = (inicio + fim) // 2
        mergesort(A, inicio, meio)
        mergesort(A, meio, fim)
        merge(A, inicio, meio, fim)
    return A

def merge(A, inicio, meio, fim):
    #exclui o 'meio'
    left = A[inicio:meio]
    right = A[meio:fim]
    i, j = 0, 0
    for k in range(inicio, fim):
        if i >= len(left):
            A[k] = right[j]
            j = j + 1
        elif j >= len(right):
            A[k] = left[i]
            i = i + 1
        elif left[i] < right[j]:
            A[k] = left[i]
            i = i + 1
        else:
            A[k] = right[j]
            j = j + 1

print(mergesort(A))