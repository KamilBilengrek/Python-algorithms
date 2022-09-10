# Quick sort
# Time complexity: O(n log(n)) - average


# pivot is last element of a list
# low - starting index, high - ending index
def quickSort(arr, low, high):
    if(low < high):
        pi = partition(arr, low, high)  # partitioning index

        quickSort(arr, low, pi-1)  #left side of correctly placed pivot
        quickSort(arr, pi+1, high)  # right side of correctly placed pivot

    return arr

def partition(arr, low, high):
    pivot = arr[high]

    i = (low - 1)  # indicates on what index should pivot be placed
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]  # placing pivot ar the correct position

    return (i+1)


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(quickSort(array, 0, len(array)-1))