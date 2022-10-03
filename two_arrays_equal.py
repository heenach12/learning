def two_arrays_equal(a1, a2):
    if len(a1) != len(a2):
        return False

    a1.sort()
    a2.sort()

    for i in range(0, len(a1)):
        if a1[i] != a2[i]:
            return False
    return True

arr1 = [3, 5, 2, 5, 2]
arr2 = [2, 3, 5, 5, 2]

print(two_arrays_equal(arr1, arr2))
