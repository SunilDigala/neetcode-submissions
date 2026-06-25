class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minSoFar = prices[0]
        max_profit = 0

        for i in prices:
            profit = i - minSoFar
            minSoFar = min(i,minSoFar)
            max_profit = max(max_profit,profit)
        
        return max_profit
        