# Binary search
# Time complexity: O(log n)

# low, high and mid are indexes
def search(arr, el, low, high):
    if high >= low:
        mid = (low + high) // 2
        if arr[mid] == el:
            return mid

        if el > arr[mid]:
            return search(arr, el, mid+1, high)
        else:
            return search(arr, el, low, mid-1)
    return -1

array = [3, 1, 4, 5, 2, 0]  # list which will be searched for an element

element = int(input("Searched element: "))

result = search(array, element, 0, len(array)-1)

if  result == -1:
    print("There is no said element in a list.")
else:
    print(f"Searched element is on index {result}.")
