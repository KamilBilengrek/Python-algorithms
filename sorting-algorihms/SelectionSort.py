# Selection sort
# Time complexity: O(n^2)


def selectionSort(arr):
    n = len(arr)  # size of an list

    for i in range(0,n):
        minimum = i
        for j in range(i,n):  # for loop to search for minimum element
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(selectionSort(array))