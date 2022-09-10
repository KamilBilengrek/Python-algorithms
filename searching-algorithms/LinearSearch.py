# Linear search
# Time complexity: O(n)


def search(arr, el):
    for i in range(len(arr)):
        if arr[i] == el:
            return i
    return -1  # if an element is not present



array = [3, 1, 4, 5, 2, 0]  # list which will be searched for an element

element = int(input("Searched element: "))

result = search(array, element)

if  result == -1:
    print("There is no said element in a list.")
else:
    print(f"Searched element is on index {result}.")
