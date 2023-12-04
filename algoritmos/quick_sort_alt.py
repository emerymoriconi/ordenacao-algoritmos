#utilizando list comprehension

def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[0]
    less = [s for s in A[1:] if s <= pivot]
    greater = [s for s in A[1:] if s > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
