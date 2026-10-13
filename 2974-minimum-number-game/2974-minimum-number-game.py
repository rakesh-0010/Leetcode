class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            for j in range(n-1):
                if nums[j] >nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        for i in range(0,n,2):  #swap each pair
            nums[i],nums[i+1]=nums[i+1],nums[i]
        return nums

    