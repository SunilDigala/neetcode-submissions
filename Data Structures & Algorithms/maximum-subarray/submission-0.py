class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum = nums[0]

        for r,value in enumerate(nums):
            curr_sum = max(0,curr_sum)
            curr_sum+= value
            max_sum = max(curr_sum,max_sum)
        return max_sum