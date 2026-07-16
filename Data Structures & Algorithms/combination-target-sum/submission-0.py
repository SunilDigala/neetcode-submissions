class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()

        def search(i,cur,total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            search(i,cur,total+nums[i])
            cur.pop()
            search(i+1,cur,total)

            
        search(0,[],0)
        return res

            

        