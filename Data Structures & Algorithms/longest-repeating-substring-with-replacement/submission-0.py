class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # maintain a map with the characters and the count
        # whenever a character count reaches 0, then you can stop and remove that key
        # however, when the len is greater than k + 1, you have to increment left
        

        m = defaultdict(int)

        left, right = 0, 0
        count = 0
        most_occuring_count = 0

        while left <= right and right < len(s):
            m[s[right]] += 1
            most_occuring_count = max(most_occuring_count, m[s[right]])
            while left <= right and right - left + 1 - most_occuring_count > k:
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    del m[s[left]]
                left += 1
            count = max(count, right - left + 1)
            right += 1
        
        return count
                    
