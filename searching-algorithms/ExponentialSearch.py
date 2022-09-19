# Exponential search
# Time complexity:


def binarySearch(arr, el, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == el:
            return mid

        if el > arr[mid]:
            return binarySearch(arr, el, mid+1, high)
        else:
            return binarySearch(arr, el, low, mid-1)
    return -1


# function for exponential search
def search(arr, el):
    # checking 1st element
    if arr[0] == el:
        return 0

    i = 1
    while i < len(array) and arr[i] <= el:
        i *= 2

    # using binary search to find the element
    return binarySearch(arr, el, i//2, min(i, len(arr)))



array = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # list which will be searched for an element

element = int(input("Searched element: "))

array.sort()  # sorting a list
result = search(array, element)

if result == -1:
    print("There is no said element in a list.")
else:
    print(f"Searched element is on index {result}.")
