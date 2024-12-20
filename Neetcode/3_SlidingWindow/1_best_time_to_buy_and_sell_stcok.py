from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price
            max_profit = max(max_profit, price - min_price)
        
        return max_profit