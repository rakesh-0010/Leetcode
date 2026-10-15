class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n=len(nums)
        for i in range(n-1):
            min=i
            for j in range(i+1,n):
                if nums[j]  < nums[min]:
                    min=j
            nums[i],nums[min]=nums[min],nums[i]

        return (nums[-1]-1)*(nums[-2]-1)
