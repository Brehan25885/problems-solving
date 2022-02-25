#!usr/bin/env/python3


'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''

 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums={}
        for i in range(0,len(nums)):
            if target-nums[i] in sums:
                return [sums[target-nums[i]],i]
            else:
                sums[nums[i]]=i
            

