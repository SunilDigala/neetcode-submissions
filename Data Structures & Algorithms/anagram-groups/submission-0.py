class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for i in strs:
            sorted_key = tuple(sorted(i))
            if sorted_key in dict.keys():
                dict[sorted_key].append(i)
            else:
                dict[sorted_key] = [i]

        return list(dict.values())