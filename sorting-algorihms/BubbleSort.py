# Bubble sort
# Time complexity: O(n^2)


def bubbleSort(arr):
    n = len(arr)  # size of an list

    for i in range(n):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(bubbleSort(array))