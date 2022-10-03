from typing import List
# this program check if any number is occuring only once and all the other numbers are appearing twice in an array.


def containsDuplicate(nums: List[int]) -> bool:
    final_value = 0
    for i in range(0, len(nums)):
        final_value = final_value ^ nums[i]
    if final_value != 0:
        return True
    return False

a = containsDuplicate(nums=[1, 2, 2, 1])
print("a is", a)
