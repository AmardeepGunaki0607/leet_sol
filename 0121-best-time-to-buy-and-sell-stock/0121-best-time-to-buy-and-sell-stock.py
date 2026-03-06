class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        profit=0
        for i in prices:
            min_price=min(min_price,i)
            profit=max(profit,i-min_price)
        return profit
        