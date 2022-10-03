def count_pairs(arr, target):
    map = {}
    count = 0

    for i in range(len(arr)):
        if target-arr[i] in map:
            count += map[target-arr[i]]
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
    return count

arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6

print(count_pairs(arr, sum))
