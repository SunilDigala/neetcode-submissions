class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        d = {}
        l,max_length = 0,0

        for r, value in enumerate(s):
            if value in d:
                l = max(l,d[value]+1)
            d[value] = r 
            max_length = max(max_length, r - l + 1)
        return max_length
        