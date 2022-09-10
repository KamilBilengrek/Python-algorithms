# Merge sort
# Time complexity: O(n log(n))


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # middle index of list
        left = arr[:mid]  # left part of list
        right = arr[mid:]  # right part of list

        # sorting both halves
        mergeSort(left)
        mergeSort(right)

        # merging final 2 sorted parts
        i = j = k = 0 # i - left part, j - right part, k - general indexing for sorted list
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # checking if every element has been used and placing missing elements on their places
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1

        while j< len(right):
            arr[k] = right[j]
            k += 1
            j += 1

    return arr


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(mergeSort(array))