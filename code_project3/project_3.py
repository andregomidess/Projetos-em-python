from random import randint
import time


# função para preencher uma lista com numeros aleatorios
def randd_intt():
    l = list()
    for _ in range(0, 5000):
        l.append(randint(1, 20000))
    return l    


def bubble_sort(array):
    for j in range(len(array)-1,0,-1):  # percorrendo o array de tras pra frente
        for i in range(j):  # laço for para percorrer todo o vetor e fazer a troca de posição se i > i+1
            if array[i]>array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1
        while low <= high and array[low] <= pivot:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


start = time.time()
array1 = randd_intt()
array2 = randd_intt()
quick_sort(array1, 0, len(array1) - 1)
end_quick = time.time()
bubble_sort(array2)
end_bubble = time.time()
print('Tempo de execução do método Bubble Sort: {:.2f} ms'.format((end_bubble - start)*1000))
print('Tempo de execução do método Quick Sort: {:.2f} ms'.format((end_quick - start)*1000))
