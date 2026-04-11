class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        for i in range(len(prices)) :
            for j in range(i,len(prices)) :
                diff = prices[j] - prices[i]
                if diff > max_price :
                    max_price = diff
        return max_price


         
            


