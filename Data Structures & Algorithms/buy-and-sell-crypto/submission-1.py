class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        ret = float('-inf')

        while left <= right and right < len(prices):
            ret = max(ret, prices[right] - prices[left])

            if prices[right] < prices[left]:
                left = right
            right += 1
        
        return ret