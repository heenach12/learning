def subarrays(a, n):
    for i in range(0, n-1):
        for j in range(i, n-1):
            for k in range(i, j+1):
                print(a[k], end= " ")
            print("   ")


a = ["a", "b", "c", "d"]
subarrays(a, len(a))
