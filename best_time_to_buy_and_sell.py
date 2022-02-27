#!usr/bin/env/python3
'''
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''

#2 pointers
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #left buy,right sell
        max_profit = 0
        while r < len(prices):
            #profitable
            if prices[l]<prices[r]:
                profit= prices[r]- prices[l]
                max_profit= max(max_profit,profit)
            else:
                l =r
            r+=1
        return max_profit
 

 ##faster sol
 class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices:
            if i<min_price:
                min_price=i
            elif i-min_price > max_profit:
                max_profit = i-min_price
        return max_profit
                



