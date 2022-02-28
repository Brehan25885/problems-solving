#!usr/bin/env/python3
'''704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        row=len(nums)
        l,r=0,len(nums)-1
        while l <=r:
            pivot =l + (r-l)//2
            if target>nums[pivot]:
                l=pivot+1
            elif target<nums[pivot]:
                r=pivot-1
            elif target == nums[pivot]:
                return pivot
        return -1
                
        
                
                
            
            


            
            


