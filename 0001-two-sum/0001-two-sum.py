class Solution(object):
    def twoSum(self, nums, target):
        dictionary={}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return [dictionary[nums[i]],i]
            else:
                    dictionary[target-nums[i]]=i