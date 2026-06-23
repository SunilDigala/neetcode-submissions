class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_position = {}

        for i,value in enumerate(nums):
            left = target - value
            if left  in dict_position.keys():
                return [dict_position[left],i]
            dict_position[value] = i  
        