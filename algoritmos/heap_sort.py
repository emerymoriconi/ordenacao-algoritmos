#Complexidade: N*logN

def constroiHeapMax(A):
    #constrói a estrutura heap
    tamHeap = len(A)
    #indice da metade para pegar todos os nós que não são folha
    i = tamHeap//2 - 1
    while i >= 0:
        refazHeapMax(A, i, tamHeap)
        i = i - 1

#garante que o nó pai seja sempre maior que seus filhos
def refazHeapMax(A, i, tamHeap):
    #zero indexado
    esquerda = (2 * i) + 1
    direita = (2 * i) + 2
    maior = i
    #se o da esquerda for maior, substitui o pai por ele
    if (esquerda < tamHeap and A[esquerda] > A[maior]):
        maior = esquerda
    #se o da direita for maior, substitui o pai por ele
    if (direita < tamHeap and A[direita] > A[maior]):
        maior = direita
    #se uma substituicao de indices tiver ocorrido, a substituicao de valores é feita
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        #conferindo se a minha troca não quebrou as regras da heap
        #se sim, refazemos a heap tendo como base o nó que foi acabado de trocar
        #pois assim vemos se ele nao quebrou as regras da heap (se ele nao é menor que os seus nós filhos)
        refazHeapMax(A, maior, tamHeap) 

def heapsort(A):
    tamHeap = len(A)
    constroiHeapMax(A)
    i = tamHeap - 1
    while i > 0:
        #troca o primeiro com o último nó
        A[i], A[0] = A[0], A[i]
        #ultimo nó (agora o maior) já está no seu lugar certo
        tamHeap = tamHeap - 1
        refazHeapMax(A, 0, tamHeap)
        i = i - 1
    return A

