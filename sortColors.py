"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]"""

from typing import List


def sortColors(nums):
    # i, lt, gt = 0, 0, len(nums) - 1
    # pivot = 1
    # while i <= gt:
    #     if nums[i] == pivot:
    #         i = i + 1
    #     elif nums[i] < pivot:
    #         nums[lt], nums[i] = nums[i], nums[lt]
    #         lt, i = lt + 1, i + 1
    #     else:
    #         nums[gt], nums[i] = nums[i], nums[gt]
    #         gt = gt - 1
    # return
    count = {0: 0, 1: 0, 2: 0}
    for x in nums:
        count[x] = count[x] + 1
    idx = 0
    for v in range(3):
        for c in range(count[v]):
            nums[idx], idx = v, idx + 1
    return


nums = [2,0,2,1,1,0]
sortColors(nums=nums)
print(nums)
