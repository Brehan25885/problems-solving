#!usr/bin/env/python3

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=[]
        dp.append(nums[0])
        largest_higgest_sum = dp[0]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
            if dp[i]>largest_higgest_sum:
                largest_higgest_sum =dp[i]
        return largest_higgest_sum

