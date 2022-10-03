from collections import defaultdict


def from collections import defaultdict


def subarraysum(arr, target):
    ws = 0
    low = 0
    high = 0

    for low in range(len(arr)):
        while ws < target and high < len(arr):
            ws += arr[high]
            high += 1

        if ws == target:
            return (low+1, (high-1)+1)

        ws -= arr[low]

arr = [1,2,3,7,5]
target = 12

a = subarraysum(arr, target)
print("a", a)

def sub_array_handling_negative_numbers(arr, target):
    prev = {}

    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum == target:
            return (0, i)

        if cur_sum-target in prev:
            return prev[cur_sum-target], i

        prev[cur_sum]= i


i, j = sub_array_handling_negative_numbers(arr, target)
print("negative", i, j)


def no_subarray_with_sum(arr, target):
    prev = defaultdict(lambda: 0)
    cur_sum = 0
    res = 0
    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum == target:
            res += 1

        if cur_sum-target in prev:
            res += prev[cur_sum-target]
        prev[cur_sum] += 1
    return res

arr2 = [1, 5, 7, -1, 5]
t = 6
w = no_subarray_with_sum(arr2, 6)
print("no of subarray ", w)(arr, target):
    ws = 0
    low = 0
    high = 0

    for low in range(len(arr)):
        while ws < target and high < len(arr):
            ws += arr[high]
            high += 1

        if ws == target:
            return (low+1, (high-1)+1)

        ws -= arr[low]

arr = [1,2,3,7,5]
target = 12

a = subarraysum(arr, target)
print("a", a)

def sub_array_handling_negative_numbers(arr, target):
    prev = {}

    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum == target:
            return (0, i)

        if cur_sum-target in prev:
            return prev[cur_sum-target], i

        prev[cur_sum]= i


i, j = sub_array_handling_negative_numbers(arr, target)
print("negative", i, j)


def no_subarray_with_sum(arr, target):
    prev = defaultdict(lambda: 0)
    cur_sum = 0
    res = 0
    for i in range(len(arr)):
        cur_sum += arr[i]

        if cur_sum == target:
            res += 1

        if cur_sum-target in prev:
            res += prev[cur_sum-target]
        prev[cur_sum] += 1
    return res

arr2 = [1, 5, 7, -1, 5]
t = 6
w = no_subarray_with_sum(arr2, 6)
print("no of subarray ", w)
