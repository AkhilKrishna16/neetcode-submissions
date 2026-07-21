class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # when you add a temperature, pop off everything that is less than the current
        # then fill result with that value
        # use indices instead of values in the stack

        s = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while s and temperatures[i] > temperatures[s[-1]]:
                idx = s.pop()
                res[idx] = i - idx
            s.append(i)
        
        return res
