def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Examples
print(bubble_sort([5, 2, 8, 1, 9]))
print(bubble_sort([3, 7, 4, 1, 6, 2]))
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))
