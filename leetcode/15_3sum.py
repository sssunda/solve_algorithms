"""

15. 3Sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        if nums.count(0) >= 3:
            result.add((0, 0, 0))
            for _ in range(nums.count(0) - 1):
                nums.remove(0)

        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return result

"""
my first solution
but, status is timelimit.

from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        nums_list = set((combinations(nums, 3)))
        for i in nums_list:
            if sum(i) == 0:
                result.add(i)

        return result
"""