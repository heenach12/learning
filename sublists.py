def sublists(arr):
    l = [[]]
    for i in range(len(arr)+1):
        for j in range(i):
            print(arr[j:i])
            l.append(arr[j:i])
    return l

arr = [1,2,3]
print(sublists(arr))
