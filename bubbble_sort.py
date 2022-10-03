def bubbble_sort(arr, n):
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

for i in arr:
    print(i, id(i), end=" ")
bubbble_sort(arr, len(arr))
print("******")

for i in arr:
    print(i, id(i), end=" ")

print("############")
print("Built in function")
arr_2 = [3, 2,56,43,34]
print("head is", id(arr_2))
for i in arr_2:
    print(i, id(i), end=" ")

arr_2.sort()

print("After sorting")
print("head is", id(arr_2))
for i in arr_2:
    print(i, id(i), end=" ")

print("############")
print("Built in function, sorted,function")
arr_3 = [7,32,90,43,12]
print("head is", id(arr_3))
for i in arr_3:
    print(i, id(i), end=" ")

d = sorted(arr_3)
print("After sorting")
print("head is", id(d))
for i in d:
    print(i, id(i), end=" ")
