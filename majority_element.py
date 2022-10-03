def majority_element(arr):
    map = {}
    for i in range(len(arr)):
        if arr[i] not in map:
            map[arr[i]] = 1
        else:
            map[arr[i]] += 1
    for key in map:
        if map[key] > len(arr)/2:
            return key
        else:
            return  0

arr = [2, 2, 2, 2, 5, 5, 2, 3, 3]
print(majority_element(arr))
