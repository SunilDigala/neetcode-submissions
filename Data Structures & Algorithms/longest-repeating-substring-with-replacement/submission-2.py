class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        l = 0
        max_char = 0
        ln = 0

        for r,value in enumerate(s):
            if value in freq:
                freq[value] = freq[value] + 1
            else:
                freq[value] = 1
            max_char = max(freq[value],max_char)
            if (r-l+1) - max_char > k:
                freq[s[l]] = freq[s[l]]-1
                l = l+1
            else:
                ln = max(r - l +1,ln)
        
        return ln



        