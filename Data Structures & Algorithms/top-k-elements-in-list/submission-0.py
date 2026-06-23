class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        g = defaultdict(int)
        for i in nums:
            g[i] = g[i]+1
        
        sorted_items = sorted(g.items(), key = lambda x : x[1], reverse = True)
        return [num for num,freq in sorted_items[:k]]


        