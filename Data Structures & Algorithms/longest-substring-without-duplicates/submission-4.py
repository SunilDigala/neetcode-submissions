class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = 0
        maxC = 0

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1      # move left past the duplicate
            seen[char] = right             # always update to latest index
            maxC = max(maxC, right - left + 1)
        return maxC



