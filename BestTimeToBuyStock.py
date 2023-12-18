class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==1:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price,price)
            max_profit = max(max_profit,price-min_price)
        return max_profit

x = Solution()
result = x.maxProfit(prices=[7, 1, 5, 3, 6, 4])
print(result)