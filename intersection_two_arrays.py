#!usr/bin/env/python3
'''
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
'''

from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        d=Counter(nums1)
        for i in nums2:
            if d[i]>0:
                ans.append(i)
                d[i]-=1
                
        return ans
            
                



