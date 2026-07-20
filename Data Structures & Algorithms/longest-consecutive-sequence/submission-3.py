class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_counter,counter = 0,0

        for i in nums_set:

            if i-1 not in nums_set:
                counter = 1

                while i+1 in nums_set:
                    counter = counter + 1
                    i = i + 1

            max_counter = max(counter,max_counter)
        return max_counter
        

                

        