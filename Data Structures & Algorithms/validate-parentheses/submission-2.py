class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        conversions = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        for i in range(len(s)):
            if s[i] in "{([":
                stack.append(s[i])
            else:
                if not stack or conversions[s[i]] != stack[-1]:
                    return False
                else:
                    stack.pop()
                
        return not stack