class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        for i in nums:
            mini = min(i,mini)
        return mini
        