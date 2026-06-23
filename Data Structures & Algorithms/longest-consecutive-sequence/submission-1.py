class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        s = sorted(nums)
        prev = s[0]
        counter = 1
        max_counter = 1

        for i in range(1,len(s)):
            if s[i] == prev+1:
                counter = counter+1
            elif s[i] == prev:
                None
            else:
                max_counter = max(max_counter,counter)
                counter = 1
            prev = s[i]
        
        return max(max_counter,counter)




        