# Insertion sort
# Time complexity: O(n^2)


def insertionSort(arr):
    n = len(arr)  # size of an list

    for i in range(1,n):
        for j in range(0,i):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]  # swapping elements

    return arr


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(insertionSort(array))
