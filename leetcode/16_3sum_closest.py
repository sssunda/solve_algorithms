"""

16. 3Sum Closest

Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 

Return the sum of the three integers. 
You may assume that each input would have exactly one solution.

My opnion:
I searched the internet for what the problem means. I didn't understand the problem.
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_num = float('inf')
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return target
                
                if abs(total-target) < abs(closest_num-target):
                    closest_num = total
                
                if total > target:
                    r -= 1
                elif total < target:
                    l += 1
                    
        return closest_num