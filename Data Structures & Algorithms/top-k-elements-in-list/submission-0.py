class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []

        c = Counter(nums)

        for key in c:
            heapq.heappush(h, (c[key], key))
            
            if len(h) > k:
                heapq.heappop(h)
        ret = []
        while h:
            ret.append(heapq.heappop(h)[1])
        
        return ret
