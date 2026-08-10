class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0
        
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
            
        return maxProfit
