class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        value = False
        dict = {}
        for i in nums:
            if i in dict.keys():
                value =  True
                break
            else:
                dict[i] = 1
        return value

        