def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [2, 7, 63, 96, 100, 45, 1]
size = len(arr)
selectionSort(arr, size)
print('The sorted array is:')
print(arr)
