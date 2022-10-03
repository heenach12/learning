from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    s = {}
    for i in range(len(nums)):
        curr_sum = target-nums[i]
        if curr_sum in s:
            return [s[curr_sum], i]
        else:
            s[nums[i]] = i


nums = [2, 7, 11, 15]
print("head of list", id(nums))
for i in nums:
    print(i, id(i))
# nums.reverse()
nums = nums[::-1]
print("head of list", id(nums))
print("reverse is", nums)
for i in nums:
    print(i, id(i))

target = 9

s = twoSum(nums=nums, target=target)
print("s is", s)

