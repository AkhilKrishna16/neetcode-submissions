class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = float('-inf')

        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                count = max(count, y - x)
        
        return count if count != float('-inf') else 0