class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse=True)
        discounts.sort(reverse=True)

        total_price=0.0

        k=min(len(prices),len(discounts))

        for i in range(k):
            total_price+= prices[i]*(100-discounts[i])/100.0

        for i in range(k,len(prices)):
            total_price+= prices[i]

        return total_price
