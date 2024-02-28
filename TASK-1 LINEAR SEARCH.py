def linearsearch(array, n, k):
    for i in range(0, n):
        if array[i] == k:
            return i
    return -1

array = list(map(int, input("Enter the elements of the array separated by space: ").split()))

while True:
    try:
        k = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")

n = len(array)
result = linearsearch(array, n, k)

if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)
