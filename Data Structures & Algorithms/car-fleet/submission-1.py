class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], speed[i]) for i in range(len(position))]
        combined.sort(reverse=True)

        s = []

        for i in range(len(combined)):
            time_taken = (target - combined[i][0]) / combined[i][1]
            if s and s[-1] < time_taken or not s:
                s.append(time_taken)

        return len(s)
            
        

        