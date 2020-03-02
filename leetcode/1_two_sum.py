"""

1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for idx_x, x in enumerate(nums[:-1]):
            y = target - x
            _nums = nums[idx_x+1:]
            if y in _nums:
                idx_y = _nums.index(y) + idx_x + 1
                return [idx_x, idx_y]