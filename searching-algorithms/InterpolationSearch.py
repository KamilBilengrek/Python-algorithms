# Interpolation search
# Time complexity:


def search(arr, el, low, high):
    # using probe position formula
    if low <= high and el >= arr[low] and el <= arr[high]:  # to make sure that indexes don't go out of range
        pos = low + ((el - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == el:
            return pos
        elif arr[pos] > el:
            search(arr, el, low, pos-1)
        else:
            search(arr, el, pos + 1, high)

    return -1  # if no elements are found


array = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # list which will be searched for an element

element = int(input("Searched element: "))

array.sort()  # sorting a list
result = search(array, element, 0, len(array)-1)

if result == -1:
    print("There is no said element in a list.")
else:
    print(f"Searched element is on index {result}.")
