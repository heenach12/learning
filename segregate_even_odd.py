def segregate_even_odd(arr):
    left = 0
    right = len(arr)-1

    while(left < right):
        while(left < right and arr[left]%2 ==0):
            left += 1


        while(left < right and arr[right]%2 ==1):
            right -= 1

        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1


arr = [12, 34, 45, 9, 8, 90, 3]
# for i in range(0, len(arr)):
#     print(arr[i], id(arr[i]))

segregate_even_odd(arr)
print("Array after segregation "),
for i in range(0, len(arr)):
    print(arr[i], end=" ")

lst = [1,2,3,4,6,7,8,9,12,4,2,5,7,2,5,2,1,4,6,3]
segregate_even_odd(lst)
print("Array after segregation "),
for i in range(0, len(lst)):
    print(lst[i], end = " ")
