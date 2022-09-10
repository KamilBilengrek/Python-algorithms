# Jump search
# Time complexity: O(√n)
import math  # for "sqrt" function


def search(arr, el):
    n = len(arr)  # size of a list
    m = int(math.sqrt(n))  # a block of numbers to jump
    lastIndex = 0

    # finding a block where searched element is present
    while arr[min(m, n) - 1] < el:
        lastIndex = m
        m += int(math.sqrt(n))
        if lastIndex >= n:
            return -1

    for i in range(lastIndex, m):
        if arr[i] == el:
            return i

    return -1  # if no elements are found


array = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # list which will be searched for an element

element = int(input("Searched element: "))

array.sort()  # sorting a list
result = search(array, element)

if  result == -1:
    print("There is no said element in a list.")
else:
    print(f"Searched element is on index {result}.")
