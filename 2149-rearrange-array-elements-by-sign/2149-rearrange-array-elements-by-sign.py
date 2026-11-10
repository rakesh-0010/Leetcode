class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        arr1=[]
        arr2=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        res = [0] * len(nums)

        a = 0
        for i in range(len(arr1)):
            res[a] = arr1[i]
            res[a + 1] = arr2[i]
            a += 2

        return res
