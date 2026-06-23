class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]
        profit = 0

        for i in prices:
            profit = max(profit,i - mini)
            mini = min(mini,i)
        
        return profit


        