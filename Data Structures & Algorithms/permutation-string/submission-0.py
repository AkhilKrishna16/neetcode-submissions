class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1 = Counter(s1)
        m2 = defaultdict(int)

        left = 0
        for right in range(len(s2)):
            m2[s2[right]] += 1
            while right - left + 1 > len(s1):
                m2[s2[left]] -= 1
                if m2[s2[left]] == 0:
                    del m2[s2[left]]
                left += 1
            if m2 == m1:
                return True
        return False
            