class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() == s[r].lower() and s[l].isalnum() and s[r].isalnum():
                l = l + 1
                r = r - 1
            elif not(s[l].isalnum()):
                l = l + 1
            elif not(s[r].isalnum()):
                r = r - 1
            else:
                return False
        
        return True
        

        