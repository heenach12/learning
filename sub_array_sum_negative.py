# from collections import defaultdict
#
#
def subArraySum(arr, n, Sum):
    # windowSum = 0
    # print(arr)
    # # maintain a window [low, high-1]
    # (low, high) = (0, 0)
    #
    # # consider every sublist starting from `low` index
    # for low in range(len(arr)):
    #
    #     # if the current window's sum is less than the given sum,
    #     # then add elements to the current window from the right
    #     while windowSum < Sum and high < len(arr):
    #         windowSum += arr[high]
    #         high = high + 1
    #
    #     # if the current window's sum is equal to the given sum
    #     if windowSum == Sum:
    #         print('Sublist found', (low+1, (high - 1)+1))
    #         return
    #
    #     # At this point, the current window's sum is more than the given sum.
    #     # Remove the current element (leftmost element) from the window
    #     windowSum -= arr[low]
    map_dict = {}
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum == Sum:
            print(0, i)

        if curr_sum-Sum in map_dict:
            return map_dict[curr_sum-Sum]+1, i

        map_dict[curr_sum] = i
    print("No subarray with given sum exists")

# arr = [0, 5, -7, 1, -4, 7, 6, 1, 4, 1, 10]
# nums = [2, 6, 0, 9, 7, 3, 1, 4, 1, 10]
nums = [1,2,3,7,5]
target = 12
# arr = [1,2,3]
# arr = [0,0,0,0,0,0,0,0,0,0]
n = len(nums)
# Sum = -3

i, j = subArraySum(arr=nums, n=n,Sum=target)
print(i, j)

from collections import defaultdict

def subArraySum2(arr, n, Sum):
    n = len(arr)
    # Dictionary to store number of subarrays
    # starting from index zero having
    # particular value of sum.
    prevSum = defaultdict(lambda: 0)
    res = 0
    # Sum of elements so far.
    currsum = 0
    for i in range(0, n):

        # Add current element to sum so far.
        currsum += arr[i]

        # If currsum is equal to desired sum,
        # then a new subarray is found. So
        # increase count of subarrays.
        if currsum == Sum:
            res += 1

            # currsum exceeds given sum by currsum  - sum.
        # Find number of subarrays having
        # this sum and exclude those subarrays
        # from currsum by increasing count by
        # same amount.
        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]

            # Add currsum value to count of
        # different values of sum.
        prevSum[currsum] += 1

    return res

arr2=[1,2,3,7,5]
Sum2=12
n= subArraySum2(arr2, len(arr2), Sum2)
print("n is", n)
