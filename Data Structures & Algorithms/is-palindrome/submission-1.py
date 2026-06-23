class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        right = len(s)-1
        output = True
        s = s.lower()

        while left < right:
            if s[left].isalnum() and s[right].isalnum() and s[left] == s[right]:
                left = left+1
                right = right - 1
            elif  not(s[left].isalnum()):
                left = left+1
            elif  not(s[right].isalnum()): 
                right = right - 1 
            elif s[left].isalnum() and s[right].isalnum() and s[left] != s[right]:
                output =  False
                break
            
        return output