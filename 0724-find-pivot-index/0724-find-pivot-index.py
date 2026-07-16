class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum=0
        left=0
        for i in range(len(nums)):
            sum+=nums[i]
        for i in range(len(nums)):
            if (left==(sum-left-nums[i])):
                return i
            left+=nums[i]
        return -1
