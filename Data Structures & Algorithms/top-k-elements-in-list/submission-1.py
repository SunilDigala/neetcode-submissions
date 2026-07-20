class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for i in nums:
            d[i] = d[i]+1
        
        a = sorted(d.items(),key = lambda x : x[1] , reverse = True )

        return [num for num, freq in a[:k]]


        