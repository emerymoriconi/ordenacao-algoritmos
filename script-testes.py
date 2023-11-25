import random
from algoritmos import bubble_sort, merge_sort, insertion_sort, quick_sort_lomuto, quick_sort_original

#define uma semente fixa
seed = 42
random.seed(seed)

#vetor decrescente de 1000 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_decrescente = sorted(random.sample(range(1, 100), 20), reverse=True)

#vetor aleatório de 20 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_aleatorio = random.sample(range(1, 1000), 20)

#vetor crescente de 1000 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_crescente = sorted(random.sample(range(1, 1000000), 1000), reverse=False)

print(vetor_decrescente)
print(quick_sort_original.quicksort_original(vetor_decrescente))