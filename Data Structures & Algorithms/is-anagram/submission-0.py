class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = Counter(s)
        m2 = Counter(t)

        return m == m2