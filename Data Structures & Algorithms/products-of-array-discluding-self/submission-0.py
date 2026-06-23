class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cp = 1
        result = []
        Zero_count = 0

        for i in nums:
            if i != 0: 
                cp = cp*i
            else:
                Zero_count+=1 

        for i in nums:
            if Zero_count>1:
                result.append(0)
            elif (Zero_count == 1 and i != 0):
                result.append(0)
            elif (Zero_count == 1 and i == 0):
                result.append(int(cp))
            elif Zero_count == 0:
                result.append(int(cp/i))
        
        return result
        


        