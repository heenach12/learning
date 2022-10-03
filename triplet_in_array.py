def triplet_in_array(arr, total_sum):
    for i in range(0, len(arr)):
        s = set()
        curr_sum = total_sum-arr[i]
        for j in range(i+1, len(arr)):
            if (curr_sum - arr[j]) in s:
                print("Triplet is", arr[i],
                      ", ", arr[j], ", ", curr_sum - arr[j])
                return True
            s.add(arr[j])

    return False

A = [1, 4, 45, 6, 10, 8]
total_sum = 22
arr_size = len(A)
triplet_in_array(A, total_sum)
