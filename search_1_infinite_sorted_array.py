def binary_search(arr, l, h):
    while (l<=h):
        mid = (l+h)//2
        if arr[mid] == 1 and (mid == 0 or arr[mid-1] == 0):
            return mid
        elif arr[mid] == 1:
            h = mid-1
        else:
            l = mid+1
    return -1


def find_occurence(arr):
    l = 0
    h = 1

    while(arr[h] == 0):
        l = h
        h = 2*h
    return binary_search(arr, l, h)


arr = [ 0, 0,0,0,0,1, 1, 1, 1, 1 ]
print(find_occurence(arr))
