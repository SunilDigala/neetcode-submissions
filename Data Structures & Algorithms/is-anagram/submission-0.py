class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
        #if tuple(s) == tuple(t):
            return True
        else:
            return False
        