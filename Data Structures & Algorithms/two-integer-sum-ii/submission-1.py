class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        d = defaultdict(int)

        for i,value in enumerate(numbers):
            if target - value in d:
                return [d[target-value],i+1]
            d[value] = i+1
        