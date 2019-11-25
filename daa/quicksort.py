def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    print('lowest {} highest {} pivot: {} '.format(i, j, pivot))

    while i <= j:
        while arr[i] <= pivot:
            i = i+1
        while arr[j] > pivot:
            j = j-1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j


def quick_sort(arr, low, high):
    if low < high:
        j = partition(arr, low, high)
        quick_sort(arr, low, j-1)
        quick_sort(arr, j+1, high)


arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quick_sort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
    print("%d" % arr[i]),
