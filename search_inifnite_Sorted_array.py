def binary_search(arr, l, r, x):
    while (l<=r):
        mid = (l + r) // 2
        if arr[mid] == x:
            return mid
        if x > arr[mid]:
            l = mid+1
        if x < arr[mid]:
            r = mid-1
    return -1
    # if r >= l:
    #     mid = l + (r - l) // 2
    #
    #     if arr[mid] == x:
    #         return mid
    #
    #     if arr[mid] > x:
    #         return binary_search(arr, l, mid - 1, x)
    #
    #     return binary_search(arr, mid + 1, r, x)
    #
    # return -1


def findPos(a, key):
    l, h, val = 0, 1, arr[0]

    while val < key:
        l = h  # store previous high
        h = 2 * h  # double high index
        val = arr[h]  # update new val

    return binary_search(a, l, h, key)


# Driver function
arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
ans = findPos(arr, 10)
if ans == -1:
    print("Element not found")
else:
    print("Element found at index", ans)
