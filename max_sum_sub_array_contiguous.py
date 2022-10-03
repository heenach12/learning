def max_sum_sub_array_contiguous(arr):
    max_so_far = float("-infinity")
    max_end_here = 0
    for i in range(len(arr)):
        max_end_here += arr[i]
        if max_so_far < max_end_here:
            max_so_far = max_end_here
        if max_end_here < 0:
            max_end_here = 0
    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_sum_sub_array_contiguous(a))
