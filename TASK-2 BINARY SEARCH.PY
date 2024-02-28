def binarySearch(array, k, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == k:
            return mid
        elif array[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return -1

array = list(map(int, input("Enter the elements of the array separated by space: ").split()))
k = int(input("Enter the number to search: "))

result = binarySearch(array, k, 0, len(array) - 1)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
