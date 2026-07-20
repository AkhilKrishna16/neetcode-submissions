class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)

        for i in range(len(strs)):
            sorted_s = sorted(strs[i])
            

            m["".join(sorted_s)].append(strs[i])
        
        ret = []
        for k in m:
            ret.append(m[k])
        
        return ret