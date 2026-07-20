class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
            res=[]
            for x in range(len(nums)):
                left=len(set(nums[:x+1]))
                right=len(set(nums[x+1:]))
                res.append(left-right)
            return res