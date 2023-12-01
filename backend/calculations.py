

from itertools import permutations
from collections import Counter

def calculate_probable_combinations(numbers_list):
    # Genera todas las permutaciones posibles de 4 dígitos
    all_permutations = [''.join(p) for p in permutations('0123456789', 4)]

    # Cuenta la frecuencia de cada permutación en los números dados
    counter = Counter(numbers_list)

    # Calcula la probabilidad de cada permutación
    probabilities = {permutation: counter.get(permutation, 0) / len(numbers_list) for permutation in all_permutations}

    # Ordena las permutaciones por probabilidad de mayor a menor
    sorted_probabilities = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)

    # Devuelve las 20 combinaciones más probables
    return sorted_probabilities[:20]
