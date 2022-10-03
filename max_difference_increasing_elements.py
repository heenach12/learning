def max_difference_increasing_elements(arr):
    arr.append(0)
    res = -1
    st = []
    for i in arr:
        if st and i <= st[-1]:
            if len(st) > 1:
                res =  max(st[-1]-st[0], res)
            while st and i <= st[-1]:
                st.pop()
        st.append(i)
    return res
    # maxv = 0
    # for i in range(0, len(arr)):
    #     for j in range(i+1, len(arr)):
    #         if (i < j and arr[i] < arr[j]):
    #             maxv =  max(maxv, arr[j] - arr[i])
    # return maxv if maxv > 0 else -1

nums = [7,1,5,4]
print(max_difference_increasing_elements(nums))
