def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])

    index = 0
    for i in range(1, len(arr)):
        if arr[index][1] >= arr[i][0]:
            arr[index][1] = max(arr[i][1], arr[index][1])
        else:
            index = index +1
            arr[index] = arr[i]
    temp = []
    for i in range(index+1):
        temp.append(arr[i])
    return temp



arr = [[6,8],[9,10],[1,3],[2,4]]
print(mergeIntervals(arr))
