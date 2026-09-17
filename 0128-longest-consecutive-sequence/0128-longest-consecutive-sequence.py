class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        max_length=1
        count=1
        for i in range(1,len(nums)):   
            if nums[i]==nums[i-1]:
                continue
            if nums[i]-nums[i-1]==1:
                count+=1
                if count>max_length:
                    max_length=count
            else:
                count=1
        return max_length