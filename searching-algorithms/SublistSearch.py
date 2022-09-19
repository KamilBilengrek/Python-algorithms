# Sublist search
# Time complexity: O(m*n)


def search(arr1, arr2):
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                i += 1
                if j == len(arr1) -1:
                    return True
            else:
                break

    return False


array1 = [7, 6, 3]  # first list
array2 = [8, 7, 6, 3, 4, 5, 2, 1, 0]  # second list

result = search(array1, array2)

if result is False:
    print("LIST NOT FOUND")
else:
    print("LIST FOUND")