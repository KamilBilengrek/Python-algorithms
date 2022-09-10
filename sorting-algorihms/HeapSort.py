# Heap sort
# Time complexity: 


# creating a binary tree and creating a max heap from it
# i - index of the root
# n - size of a list
def heapify(arr, i, n):
    root = i # root of the tree
    left = 2*i + 1  # index of left element of the root
    right = 2*i + 2  # index of right element of the root

    # checking if elements on both sides exist and if they are bigger than root
    if left < n and arr[root] < arr[left]:
        root = left

    if right < n and arr[root] < arr[right]:
        root = right

    if root != i:
        arr[i], arr[root] = arr[root], arr[i]

        # heapify the root
        heapify(arr, root, n)


def heapSort(arr):
    # creating a max-heap
    for i in range(len(arr)//2 - 1, -1, -1):
        heapify(arr,i,len(arr))

    # sorting
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

    return arr


array = [3, 1, 4, 5, 2, 0]  # list which will be sorted

print(heapSort(array))