class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        marked = set()
        count = 0

        while left <= right and right < len(s):
            while right < len(s) and s[right] in marked:
                marked.remove(s[left])
                left += 1
            
            count = max(count, right - left + 1)
            marked.add(s[right])
            right += 1
        
        return count