import random
import numpy as np
from algoritmos import bubble_sort, merge_sort, insertion_sort, quick_sort_lomuto, quick_sort_original, quick_sort_alt

#arquivo dedicado à geração dos vetores, salvando-os em 3 diferentes arquivos txt 
#define uma semente fixa
seed = 42
random.seed(seed)

#vetor decrescente de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_decrescente = sorted(random.sample(range(1, 10000), 500), reverse=True)

#vetor aleatório de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_aleatorio = random.sample(range(1, 100), 20)

#vetor crescente de 500 elementos (ajustar a quantidade de acordo com a necessidade)
vetor_crescente = sorted(random.sample(range(1, 10000), 500), reverse=False)

#caminho para salvar os arquivos de texto
caminho_arquivo_decrescente = 'vetor_decrescente.txt'
caminho_arquivo_aleatorio = 'vetor_aleatorio.txt'
caminho_arquivo_crescente = 'vetor_crescente.txt'

#salva os vetores em arquivos de texto
np.savetxt(caminho_arquivo_decrescente, vetor_decrescente, fmt='%d')
np.savetxt(caminho_arquivo_aleatorio, vetor_aleatorio, fmt='%d')
np.savetxt(caminho_arquivo_crescente, vetor_crescente, fmt='%d')