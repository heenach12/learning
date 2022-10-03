"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

"""

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    lst = [1] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                lst[i] = max(lst[i], 1 + lst[j])
    return max(lst)

nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums=nums))
